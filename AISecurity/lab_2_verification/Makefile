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

EPOCHS ?= 5
EPS ?= 0.01
NETWORK ?= onnx_models/wine_classifier.onnx
RESULTS ?= results

load-wine-data:
	python 05_load_wine_data.py

train-wine:
	python 06_train_wine_quality_predictor.py --epochs $(EPOCHS)

train-wine-robust:
	python 06_train_wine_quality_predictor.py --epochs $(EPOCHS) --robust --specification 06_wine.vcl

verify-wine-robust:
	vehicle verify \
		--specification 06_wine.vcl \
		--network classifier:$(NETWORK) \
		--parameter epsilon:$(EPS) \
		--dataset trainingInputs:data/wine/wine-features.idx \
		--dataset trainingLabels:data/wine/wine-labels.idx \
		--property robust \
		--solver Marabou

verify-wine-alcohol:
	vehicle verify \
		--specification 06_wine.vcl \
		--network classifier:$(NETWORK) \
		--parameter epsilon:$(EPS) \
		--dataset trainingInputs:data/wine/wine-features.idx \
		--dataset trainingLabels:data/wine/wine-labels.idx \
		--property highAlcoholIsGood \
		--solver Marabou

run-wine:
	mkdir -p $(RESULTS)
	make load-wine-data >> $(RESULTS)/wine_results_$(EPOCHS)_epochs.txt 2>&1
	make train-wine >> $(RESULTS)/wine_results_$(EPOCHS)_epochs.txt 2>&1
	make verify-wine-robust EPS=0.005 >> $(RESULTS)/wine_results_$(EPOCHS)_epochs.txt 2>&1
	make verify-wine-robust EPS=0.01 >> $(RESULTS)/wine_results_$(EPOCHS)_epochs.txt 2>&1
	make verify-wine-robust EPS=0.05 >> $(RESULTS)/wine_results_$(EPOCHS)_epochs.txt 2>&1
	make verify-wine-alcohol >> $(RESULTS)/wine_results_$(EPOCHS)_epochs.txt 2>&1

run-wine-robust:
	mkdir -p $(RESULTS)
	make train-wine-robust >> $(RESULTS)/wine_results_$(EPOCHS)_epochs_robust.txt 2>&1
	make verify-wine-robust NETWORK=onnx_models/wine_robust_classifier.onnx EPS=0.005 >> $(RESULTS)/wine_results_$(EPOCHS)_epochs_robust.txt 2>&1
	make verify-wine-robust NETWORK=onnx_models/wine_robust_classifier.onnx EPS=0.01 >> $(RESULTS)/wine_results_$(EPOCHS)_epochs_robust.txt 2>&1
	make verify-wine-robust NETWORK=onnx_models/wine_robust_classifier.onnx EPS=0.05 >> $(RESULTS)/wine_results_$(EPOCHS)_epochs_robust.txt 2>&1