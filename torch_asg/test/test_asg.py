import torch
from torch_asg.asg import ASG
import torch_asg_native


def test_run():
    C = 7
    T = 6
    N = 1
    S = 5

    asg_loss = ASG(n_vocab=C)
    # asg_loss.forward(log_probs=torch.randn(T, N, C),
    #                  targets=torch.randint(0, C, (N, S)),
    #                  input_lengths=torch.randint(1, T + 1, (N,)),
    #                  target_lengths=torch.randint(1, S + 1, (N,)))

    result = torch_asg_native.fac_forward(asg_loss.transition,
                                          torch.randn(T, N, C),
                                          torch.randint(0, C, (N, S)),
                                          torch.randint(T, T + 1, (N,)),
                                          torch.randint(S, S + 1, (N,)),
                                          'none',
                                          'none')
    print(result[0].shape)
    print(result[0])
    print(result[1])
    print(result[2])
    print(result[3])