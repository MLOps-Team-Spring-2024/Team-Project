import torch
import pytest
import os
from mlops_team_project.models import xgboost_model as model


def test_accuracy():
    assert model.pytest_train_accuray == model.pytest_test_accuracy

def test_x_training():
    assert model.pytest_X_train == model.pytest_X_test

def test_y_training():
    assert model.pytest_y_train == model.pytest_y_test