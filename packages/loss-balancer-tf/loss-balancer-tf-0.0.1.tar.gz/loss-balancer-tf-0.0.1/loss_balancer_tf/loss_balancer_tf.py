import tensorflow as tf
import typing as tp

# 元の実装: https://github.com/facebookresearch/encodec/blob/main/encodec/balancer.py
class LossBalancer():
    def __init__(self,
                 weights: tp.Dict[str, float],
                 rescale_grads: bool=True,
                 total_norm: float=1.0,
                 epsilon: float=1e-12,
                 ema_decay: float=0.999):
        self.loss_weights = weights
        self.rescale_grads = rescale_grads
        self.total_norm = total_norm
        self.epsilon = epsilon
        self.ema_decay = ema_decay

        self.total = tf.Variable(tf.zeros(len(self.loss_weights)), trainable=False)
        self.fix = tf.Variable(tf.zeros(len(self.loss_weights)), trainable=False)
        self.keys_to_indices = {k: i for i, k in enumerate(self.loss_weights)}

    def _update(self, metrics: tp.Dict[str, tp.Any], weight: float = 1) -> tp.Dict[str, float]:
        for key, value in metrics.items():
            idx = self.keys_to_indices[key]
            self.total[idx].assign(self.total[idx] * self.ema_decay + weight * value)
            self.fix[idx].assign(self.fix[idx] * self.ema_decay + weight)
            
        return {key: self.total[self.keys_to_indices[key]] / self.fix[self.keys_to_indices[key]]
                    for key in metrics.keys()}

    def gradient(self, loss_dict: tp.Dict[str, tf.Tensor], tape: tf.GradientTape, trainable_variables):
        total_weights = sum(list(self.loss_weights.values()))
        ratios = {k: w / total_weights for k, w in self.loss_weights.items()}

        norms = {}
        grads = {}
        for name, loss in loss_dict.items():
            gradients = tape.gradient(loss, trainable_variables)
            norms[name] = tf.linalg.global_norm(gradients)
            grads[name] = gradients

        avg_norms = self._update(norms)
        metrics = {}
        total = sum(avg_norms.values())
        for k, v in avg_norms.items():
            metrics[f'ratio_{k}'] = v / total

        out_grads = None
        for name, grad_list in grads.items():
            if self.rescale_grads:
                scale = ratios[name] * self.total_norm / (self.epsilon + avg_norms[name])
                scaled_grad_list = [tf.multiply(grad, scale) if grad is not None else grad for grad in grad_list]
            else:
                weight = self.loss_weights[name]
                scaled_grad_list = [tf.multiply(grad, weight) if grad is not None else grad for grad in grad_list]

            if out_grads is None:
                out_grads = scaled_grad_list
            else:
                out_grads = [
                    tf.add(out_grad, scaled_grad)
                    if out_grad is not None and scaled_grad is not None else out_grad or scaled_grad
                    for out_grad, scaled_grad in zip(out_grads, scaled_grad_list)]

        return out_grads, metrics


def test():
    x = tf.Variable([0.0], trainable=True)
    one = tf.constant([1.0])
    minus_one = tf.constant([-1.0])

    balancer_no_rescale = LossBalancer(weights={'1': 1, '2': 1}, rescale_grads=False)
    with tf.GradientTape(persistent=True) as tape:
        loss_1 = tf.reduce_mean(tf.abs(x - one))
        loss_2 = 100 * tf.reduce_mean(tf.abs(x - minus_one))
        losses = {'1': loss_1, '2': loss_2}
    grads_no_rescale, _ = balancer_no_rescale.gradient(losses, tape, [x])
    assert tf.abs(grads_no_rescale - tf.constant(99.0)) < 1e-5


    balancer_rescale = LossBalancer(weights={'1': 1, '2': 1}, rescale_grads=True)
    with tf.GradientTape(persistent=True) as tape:
        loss_1 = tf.reduce_mean(tf.abs(x - one))
        loss_2 = 100 * tf.reduce_mean(tf.abs(x - minus_one))
        losses = {'1': loss_1, '2': loss_2}
    grads_rescale, _ = balancer_rescale.gradient(losses, tape, [x])

    assert tf.abs(grads_rescale) < 1e-5

if __name__ == '__main__':
    test()