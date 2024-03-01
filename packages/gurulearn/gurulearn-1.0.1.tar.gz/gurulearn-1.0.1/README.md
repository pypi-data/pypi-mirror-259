python setup.py sdist bdist_wheel
pip install dist/gurulearn-1.0.0-py3-none-any.whl

linear regression:
# plot_linear_regression(csv_file, x_name, y_name, x_element, y_element)
# linear_regression_accuracy(csv_file, x_name, y_name, x_element, y_element)

vgg:
# vgg_train("train", "test", 1)           # Train for 5 epochs using CPU (default)
# vgg_train("train_dataset", "test_dataset", 5, "cuda")   # Train for 5 epochs using CUDA
# vgg_train("train_dataset", "test_dataset", 5, "cpu")    # Train for 5 epochs using CPU