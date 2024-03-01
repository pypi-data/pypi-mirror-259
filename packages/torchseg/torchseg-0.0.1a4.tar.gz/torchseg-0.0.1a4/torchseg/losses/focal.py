from functools import partial
from typing import Optional

import torch
import torch.nn as nn

from ._functional import focal_loss_with_logits
from .constants import BINARY_MODE, MULTICLASS_MODE, MULTILABEL_MODE


class FocalLoss(nn.Module):
    def __init__(
        self,
        mode: str,
        alpha: Optional[float] = None,
        gamma: Optional[float] = 2.0,
        ignore_index: Optional[int] = None,
        reduction: Optional[str] = "mean",
        normalized: bool = False,
        reduced_threshold: Optional[float] = None,
        classes: Optional[list[int]] = None,
    ):
        """Compute Focal loss

        Args:
            mode: Loss mode 'binary', 'multiclass' or 'multilabel'
            alpha: Prior probability of having positive value in target.
            gamma: Power factor for dampening weight (focal strength).
            ignore_index: If not None, targets may contain values to be ignored. Target
                values equal to ignore_index will be ignored from loss computation.
            normalized: Use normalized focal loss (https://arxiv.org/pdf/1909.07829.pdf)
            reduced_threshold: Switch to reduced focal loss.
                Note, when using this mode you should use `reduction="sum"`.
            classes:  List of classes that contribute in loss computation.
                By default, all channels are included. Only supported in multiclass mode

        Shape
             - **y_pred** - torch.Tensor of shape (N, C, H, W)
             - **y_true** - torch.Tensor of shape (N, H, W) or (N, C, H, W)

        Reference
            https://github.com/BloodAxe/pytorch-toolbelt

        """
        assert mode in {BINARY_MODE, MULTILABEL_MODE, MULTICLASS_MODE}
        super().__init__()

        self.mode = mode
        self.ignore_index = ignore_index
        self.classes = classes
        self.focal_loss_fn = partial(
            focal_loss_with_logits,
            alpha=alpha,
            gamma=gamma,
            reduced_threshold=reduced_threshold,
            reduction=reduction,
            normalized=normalized,
        )

    def forward(self, y_pred: torch.Tensor, y_true: torch.Tensor) -> torch.Tensor:
        if self.mode in {BINARY_MODE, MULTILABEL_MODE}:
            y_true = y_true.view(-1)
            y_pred = y_pred.view(-1)

            if self.ignore_index is not None:
                # Filter predictions with ignore label from loss computation
                not_ignored = y_true != self.ignore_index
                y_pred = y_pred[not_ignored]
                y_true = y_true[not_ignored]

            loss = self.focal_loss_fn(y_pred, y_true)

        elif self.mode == MULTICLASS_MODE:
            num_classes = y_pred.size(1)
            loss = 0

            # Filter anchors with -1 label from loss computation
            if self.ignore_index is not None:
                not_ignored = y_true != self.ignore_index

            for cls in range(num_classes):
                if self.classes is None or cls in self.classes:
                    cls_y_true = (y_true == cls).long()
                    cls_y_pred = y_pred[:, cls, ...]

                    if self.ignore_index is not None:
                        cls_y_true = cls_y_true[not_ignored]
                        cls_y_pred = cls_y_pred[not_ignored]

                    loss += self.focal_loss_fn(cls_y_pred, cls_y_true)

        return loss
