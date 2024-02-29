from torch import nn
import torch.nn.init as init

def init_weights(model, conv=None, batchnorm=None, linear=None, lstm=None):
    """
    :param model: Pytorch Model which is nn.Module
    :param conv:  'kaiming' or 'xavier'
    :param batchnorm: 'normal' or 'constant'
    :param linear: 'kaiming' or 'xavier'
    :param lstm: 'kaiming' or 'xavier'
    """
    for m in model.modules():
        if conv is not None and isinstance(m, (nn.modules.conv._ConvNd)):
            if conv == 'kaiming':
                init.kaiming_normal_(m.weight)
            elif conv == 'xavier':
                init.xavier_normal_(m.weight)
            else:
                raise ValueError("init type of conv error.\n")
            if m.bias is not None:
                init.constant_(m.bias, 0)

        elif batchnorm is not None and isinstance(m, (nn.modules.batchnorm._BatchNorm)):
            if batchnorm == 'normal':
                init.normal_(m.weight, 1.0, 0.02)
            elif batchnorm == 'constant':
                init.constant_(m.weight, 1.0)
            else:
                raise ValueError("init type of batchnorm error.\n")
            init.constant_(m.bias, 0.0)

        elif linear is not None and isinstance(m, nn.Linear):
            if linear == 'kaiming':
                init.kaiming_normal_(m.weight)
            elif linear == 'xavier':
                init.xavier_normal_(m.weight)
            else:
                raise ValueError("init type of linear error.\n")
            if m.bias is not None:
                init.constant_(m.bias, 0)

        elif lstm is not None and isinstance(m, nn.LSTM):
            for name, param in m.named_parameters():
                if 'weight' in name:
                    if lstm == 'kaiming':
                        init.kaiming_normal_(param)
                    elif lstm == 'xavier':
                        init.xavier_normal_(param)
                    else:
                        raise ValueError("init type of lstm error.\n")
                elif 'bias' in name:
                    init.constant_(param, 0)

def official_init(model):
    # Official init from torch repo.
    for m in model.modules():
        if isinstance(m, nn.Conv2d):
            nn.init.kaiming_normal_(m.weight)
        elif isinstance(m, nn.BatchNorm2d):
            nn.init.constant_(m.weight, 1)
            nn.init.constant_(m.bias, 0)
        elif isinstance(m, nn.Linear):
            nn.init.constant_(m.bias, 0)