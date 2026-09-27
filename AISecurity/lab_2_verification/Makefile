run-acas-xu-1-7:
	vehicle verify \
		--specification acasXu.vcl \
		--solver Marabou \
		--network acasXu:tutorial/chapter-2/chapter-code/acasXu_1_7.onnx \
		--property property3

run-acas-xu-1-8:
	vehicle verify \
		--specification acasXu.vcl \
		--solver Marabou \
		--network acasXu:tutorial/chapter-2/chapter-code/acasXu_1_8.onnx \
		--property property3

run-acas-xu-1-9:
	vehicle verify \
		--specification acasXu.vcl \
		--solver Marabou \
		--network acasXu:tutorial/chapter-2/chapter-code/acasXu_1_9.onnx \
		--property property3

run-mnist:
	vehicle verify \
	--specification mnist.vcl \
	--network classifier:tutorial/chapter-3/chapter-code/mnist-classifier.onnx \
	--parameter epsilon:0.005 \
	--dataset trainingImages:tutorial/chapter-3/chapter-code/t2-images.idx \
	--dataset trainingLabels:tutorial/chapter-3/chapter-code/t2-labels.idx \
	--solver Marabou
