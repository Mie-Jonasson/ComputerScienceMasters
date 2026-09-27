run-acas-xu-1-7:
	vehicle verify \
		--specification 02_acasXu.vcl \
		--solver Marabou \
		--network acasXu:tutorial/chapter-2/chapter-code/acasXu_1_7.onnx \
		--property property3

run-acas-xu-1-8:
	vehicle verify \
		--specification 02_acasXu.vcl \
		--solver Marabou \
		--network acasXu:tutorial/chapter-2/chapter-code/acasXu_1_8.onnx \
		--property property3

run-acas-xu-1-9:
	vehicle verify \
		--specification 02_acasXu.vcl \
		--solver Marabou \
		--network acasXu:tutorial/chapter-2/chapter-code/acasXu_1_9.onnx \
		--property property3

run-mnist:
	vehicle verify \
	--specification 03_mnist.vcl \
	--network classifier:tutorial/chapter-3/chapter-code/mnist-classifier.onnx \
	--parameter epsilon:0.005 \
	--dataset trainingImages:tutorial/chapter-3/chapter-code/t2-images.idx \
	--dataset trainingLabels:tutorial/chapter-3/chapter-code/t2-labels.idx \
	--solver Marabou

train-fashion-mnist:
	python 04_fashion_mnist.py

train-fashion-mnist-robust:
	python 04_fashion_mnist.py --robust --specification tutorial/chapter-4/chapter-code/fmnist-robustness.vcl

verify-fashion-mnist:
	vehicle verify \
		--specification tutorial/chapter-3/exercises/FMNIST/fashionRobustness-solution.vcl \
		--network classifier:onnx_models/vanilla_classifier.onnx \
		--parameter epsilon:0.005 \
		--dataset trainingImages:tutorial/chapter-3/exercises/FMNIST/idxdata/0-49Images.idx \
		--dataset trainingLabels:tutorial/chapter-3/exercises/FMNIST/idxdata/0-49Labels.idx \
		--solver Marabou

verify-fashion-mnist-robust:
	vehicle verify \
		--specification tutorial/chapter-4/chapter-code/fmnist-robustness.vcl \
		--network classifier:onnx_models/robust_classifier.onnx \
		--parameter epsilon:0.005 \
		--dataset trainingImages:tutorial/chapter-3/exercises/FMNIST/idxdata/0-49Images.idx \
		--dataset trainingLabels:tutorial/chapter-3/exercises/FMNIST/idxdata/0-49Labels.idx \
		--solver Marabou

load-wine-data:
	python 05_load_wine_data.py