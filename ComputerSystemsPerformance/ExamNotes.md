# What is the exam like?
Message from Pinar:
```
The students from the same group are scheduled back-to-back.
Omar and I both will be at the exam in addition to an external censor.

The exam is mainly based on your projects, but the topics we covered in class are also included.
You can consider the exam having four parts:
(1) questions on your first project assignment (~6mins)
(2) questions on your second project assignment (~6mins)
(3) one-two general questions on the class topics (~5mins)
(4) grading & feedback

You don't need to prepare a presentation.

You can have your project reports with you and point to some results/figures if it helps your explanation.

The topics we covered in class are also relevant for your projects as they will be helpful when it comes to explaining some of the performance behavior, so you could be asked some general questions as we discuss your projects as well.
For example, if you are running experiments on two different kinds of processors, a relevant question could be: why are the results on one faster than the other? Is it just the clock speed or is there a difference between the cache hierarchy / storage?
Or what is the impact of OS to your results (especially with respect to experiments with thread pinning)?
Or if there is a behavior that you cannot explain, a question could be what type of experiment you would design to help explaining this if you had the time?

For the general course topics, I recommend reminding yourselves what we covered by going over the course slides and exercises.

Don't hesitate to ask if you have any questions.
```

# To-Dos

- [ ] Print Project Reports
- [ ] Read-through and highlight relevant parts of the project reports (f.ex. all figures and conclusions)
- [ ] Write down main points and takeaways from projects
- [ ] Get handwritten notes from the Ipad and copy them into this repo
- [ ] Go through slides and write down takeaways, terminology etc. in an easy overview
- [ ] Go through exercises and write down outcomes and discussions
- [ ] Write up a terminology overview used in projects, exercises and curriculum
- [ ] Rehearse talking out loud about the projects
- [ ] Rehearse talking out loud about course curriculum
- [ ] Unexplained / Weak results; what would we do different?

# Project Walk-through

# Curriculum Walk-through

## Lecture 1 - Performance Analysis & Experimental Design

The *systems stack* defines the system we are running things on and has multiple layers. Namely, it has the **aplication** which is software programs etc. that are running on top of the **operating system** (linux / windows / MacOS etc.) which is running on the **hardware** (servers, disks etc.). Each of these **highlighted** items are a layer for themselves that may or may not be interchanged as part of an experiment design, if the goal is to compare multiple *systems*.

When we are investigating systems, we are interested in defining **metrics** that we can measure, **workloads** that we can run and **systems** we want to test. The system also encompasses *parameters* (often denoted k) which have a defined set of *levels* (often deonted l) to run the experiment on.
We also need tools that help us run and investigate the performance - i.e. we are reasoning among the *system layers* about why certain experiments perform in a certain way.

**Experiment** is defined as something that does either of below:
- *Makes a Discovery* - what is the throughput of A? How long does it take to fine-tune ML model B?
- *Tests a Hypothesis* - Hypothesis: fine-tuning model A is faster than fine-tuning model B
- *Demonstrates a Known Fact* - Reproduce the proof that fine-tuning model A is faster than fine-tuning model B, to confirm

We also **NEVER** run an experiment just once - we need to run many times and make sure the standard deviation between runs is low - i.e., we need to ensure that our results are reproducible and not an outlier!

### Workloads
If the system is the hardware itself, the workload may be anything in the system stack from the OS and up.
If the system is some software or tooling, the workload may be a specific task performed by the software, such as model training and inference.
The workloads

There are three main workload options:
- *synthetic*, i.e. benchmarking data, selected and created for a specific purpose
- *trace-base*, i.e. historical workloads from logs or similar, imitating the expected real-life application
- *actual*, i.e. we run it directly in real time

### Metrics
Metrics are what we measure and compare between different configurations in order to gain some kind of insight into how well a particular system is solving whatever task we put it up to.
Metrics should therefore also be tightly linked with the research question / goal, such that we can infer something about our point-of-interest using the metrics.

There are as many types of metrics as you can possibly think of, but some common ones are:
- *throughput* - how many requests are processed in unit time?
- *latency* - how much time passes from stimulation to response?
- *energy* - how much power is spent on a request?
- *memory footprint* - how much memory space is used?
- *CPU utilization* - how much are the cores being used?
- *ease of use*, *cache misses*, *security*, etc.

### Parameters and Levels
When running experiments it can be difficult to decide exactly what to test and which combinations. Doing a full search on the entire space of parameters may be infeasible, when either the number of parameters (k) of levels (l) grow large!
I.e. because we are have 3 parameters with each 8 levels, testing all possible combinations will give us 8^3 experiments :o

A better option is to decide on a *default level* for each parameter such that only a single parameter is varied at a time away from this default level! In the example above, this would instead be 8 + (8-1) + (8-1) :D
It is also common to try multiple default values to give a broader picture.

### 2^k factorial experiment
Is a particular type of experiment aiming to measure which effect each parameter has on the output. It works as follows:
- Decide for a low and high level for each parameter (2 values)
- Run experiments for all combinations (2^k total experiments) - with repetitions!
- Using the non-linear regression where each parameter defines a variable x_i, which has the value -1 for the low level and 1 for the high level. See example here:

![](images/2k_factorial.png)

### Overview

![](images/performance_analysis.png)

## Lecture 2 - Memory Hierarchy & Parallelism

## Lecture 3 - Profiling

## Lecture 4 - Queueing Theory, Common Mistakes, Plotting Graphs

## Lecture 5 - Operating Systems

## Lecture 6 - Benchmarking

## Lecture 7 - Storage Devices

## Lecture 8 - Oracle Guest Lecture

## Lecture 9 - Hardware Acceleration & GPUs

## Lecture 10 - AI Performance

## Lecture 11 - Cloud

## Lecture 12 - Snowflake Guest Lecture

# Exercise Walkthrough