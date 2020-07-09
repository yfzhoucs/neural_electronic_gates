from . import gate_in1out1, gate_in2out1
import torch.nn as nn
import torch


class Gate(nn.Module):
    def __init__(self, name, ckpt_path_dict):
        super(Gate, self).__init__()
        assert name in ckpt_path_dict
        self.name = name
        if name == 'not':
            self.gate = gate_in1out1.GateIn1Out1()
        else:
            self.gate = gate_in2out1.GateIn2Out1()
        self.gate.load_state_dict(torch.load(
            ckpt_path_dict[name]
        ))

    def forward(self, *x):
        return self.gate(*x)