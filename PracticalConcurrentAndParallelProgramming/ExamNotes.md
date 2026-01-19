# Topic Notes
## 1. **Intro to concurrency and the mutual exclusion problem**: Define and motivate concurrency and mutual exclusion. Explain data races, race conditions, and critical sections. Show some examples of code from your solutions to the exercises in week 1.
- *Concurrency* can be used to speed up computation time by dividing the work between multiple actors/threads.
    - Hidden: Sequential computers might do *time-sharing* (giving the experience that multiple things are executed simultaneously, but single resource)
    - Exlploitation: Today, we have computers that can simultaneously execute instructions over multiple cores
- *Mutual Exclusion* is a set of rules for ensuring that a concurrent program runs without problems.
    - Only 1 thread in critical section at a time
    - avoiding deadlocks - threads must leave the critical section eventually ("try, finally" to always unlock)
    - avoiding starvation - threads must enter the critical section eventually (scheduler makes this decision)
- *Data Races* is when two threads access the same memory resource at the same time, and at least one of them is a modification operation - f.ex. reading/writing current value of shared variable.
- *Race Conditions* is when the output of the programme depends on the interleaving of threads - f.ex. 
- These two types of races may occur jointly or separately - i.e. something may be both or just one of the two.
    - A data race may not impact the output of the program
    - A race condition may not be related to shared memory
- *Critical Sections* is the lines of code that has data races and should always be minimal

## 2. **Synchronization**: Explain and motivate how locks, monitors, and semaphores can be used to address the challenges caused by concurrent access to shared memory. Show some examples of code from your solutions to the exercises in week 2.
- *Locks* are used around a critical section to ensure only 1 thread enters at a time. One of the waiting threads will be picked at random once lock is available.
- *Monitors* are used to solve the *Reader-Writer Problem* (i.e. only 1 writer or any number of readers). Keeps track of *internal state, methods & conditions*, for reader-writer this is for example keeping track whether the lock holder is a writer or reader, keeping track of the number of active readers and waiting / notifying on condition changing.
- *Semaphores* TODO
- *Fairness* for different access types, i.e. in monitors Writer may wait forever if we allow new readers into the section while the write is still waiting. (starvation issue!)

## 3. **Visibility**: Explain the problems of visibility and reordering in shared memory concurrency. Motivate and describe the use of volatile variables and locks to tackle these problems. Show some examples of code from your solutions to the exercises in week 2.
- *Visibility*: CPUs are allowed to keep data (such as variable values) in registers / cache, that is then unavailable to other CPUs. The program stores data here, because it reduces latency for the thread to get and update the data.
    - flushing to main memory may be ensured using `lock`/`unlock` or `volatile` variables. This will make shared variables' updated value available across all CPUs.
- *Reordering*: the compiler may reorder instructions of the programme as to optimize performance. This may cause weird behavior, where critical sections are interleaved in an undesireable way.
    - using `synchronized` around two sections ensures that the steps of these sections are NOT interleaved with each other. One has the execute one section in full before executing the other section.

## 4. **Java memory model**: Motivate the need for the Java memory model. Explain the elements of the Java memory model including program order, happens-before order, synchronization order, and data races. Define what a correctly synchronized program is according to the Java memory model. Show some examples of code from your solutions to the exercises in week 3 and illustrate the use of the Java memory model to reason about their correctness.

## 5. **Thread-safe classes**: Define and explain what makes a class thread-safe. Explain the issues that may make classes not thread-safe. Show some examples of code from your solutions to the exercises in week 4.

## 6. **Testing**: Explain the challenges in ensuring the correctness of concurrent programs. Describe different testing strategies for concurrent programs, and their advantages and disadvantages. Show some examples of code from your solutions to the exercises in week 5.

## 7. **Performance measurements**: Motivate and explain how to measure the performance of Java code. Illustrate some of the pitfalls there are in doing such measurements. Show some examples of code from your solutions to the exercises in week 9.

## 8. **Performance and Scalability**: Explain how to increase the performance of Java code exploiting concurrency. Illustrate some of the pitfalls there are in doing this. Show some examples of code from your solutions to the exercises in week 10.

## 9. **Lock-free Data Structures**: Define and motivate lock-free data structures. Explain how *compare-and-swap* (CAS) operations can be used to solve concurrency problems. Show some examples of code from your solutions to the exercises in week 6.

## 10. **Linearizability**: Explain and motivate linearizability. Explain how linearizability can be applied to reason about the correctness of concurrent objects. Show some examples of code in your solutions to the exercises in week 7 where you used linearizability to reason about correctness.

## 11. **Streams**: Explain and motivate the use of streams to parallelize computation. Discuss issues that arise in operations executed by parallel streams. Show some examples of code from your solutions to the exercises in week 11.

## 12. **Message Passing**: Explain and motivate the actor model of concurrent computation. Discuss advantages and disadvantages of approaches to distribute computation in actor systems. Show some examples of code from your solutions to the exercises in week 12 and 13.

# Code Examples
## Question 1
```[java]
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class CounterThreads2Covid {

    long counter = 0;
    final long PEOPLE  = 10_000;
    final long MAX_PEOPLE_COVID = 15_000;
    Lock l = new ReentrantLock();

    public CounterThreads2Covid() {
        try {
            Turnstile turnstile1 = new Turnstile();
            Turnstile turnstile2 = new Turnstile();

            turnstile1.start();turnstile2.start(); // start two threads
            turnstile1.join();turnstile2.join(); // join two threads

            System.out.println(counter+" people entered"); // check threads stopped at correct count
        }
        catch (InterruptedException e) {
            System.out.println("Error " + e.getMessage());
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new CounterThreads2Covid();
    }


    public class Turnstile extends Thread {

        public void run() {
            for (int i = 0; i < PEOPLE; i++) {
                l.lock(); // critical section between lock/unlock; evaluating / updating shared variable
                try {
                    if (counter >= MAX_PEOPLE_COVID) {
                        return;
                    }
                    counter++;
                } finally { // use try-finally to always unlock, avoiding deadlocks
                    l.unlock();
                }
            }
        }
    }
}
```

## Question 2
```[java]
public class FairReadWriteMonitor {
    private int readers         = 0;
    private boolean writer      = false;

    public synchronized void readLock() {
        try {
            while(writer)
                this.wait();
            readers++;
        }
        catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public synchronized void readUnlock() {
        readers--;
        if(readers==0)
            this.notifyAll();
    }

    public synchronized void writeLock() {
        try {
            while(writer)
                this.wait();
            writer=true;
            while(readers > 0)
                this.wait();
        }
        catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public synchronized void writeUnlock() {
        writer=false;
        this.notifyAll();
    }
}
```

## Question 3
```[java]
public class TestMutableInteger {
    public static void main(String[] args) {
        final MutableInteger mi = new MutableInteger();
        Thread t = new Thread(() -> {
                while (mi.get() == 0)        // Loop while zero
                    {/* Do nothing*/ }
                System.out.println("I completed, mi = " + mi.get());
        });
        t.start();
        try { Thread.sleep(500); } catch (InterruptedException e) { e.printStackTrace(); }
        mi.set(42);
        System.out.println("mi set to 42, waiting for thread ...");
        try { t.join(); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.println("Thread t completed, and so does main");
    }
}

class MutableInteger {
    // WARNING: Not ready for usage by concurrent programs
    private volatile int value = 0;
    public void set(int value) {
        this.value = value;
    }
    public int get() {
        return value;
    }
}
```

## Question 4
```[java]
```

## Question 5
```[java]
```

## Question 6
```[java]
```

## Question 7
```[java]
```

## Question 8
```[java]
```

## Question 9
```[java]
```

## Question 10
```[java]
```

## Question 11
```[java]
```

## Question 12
```[erlang]
```

# General Notes
## Abstract Syntaxes
### Interleaving
\<thread>(\<step>), \<thread>(\<step>), ...

## Java Modifiers
- **Synchronized methods** `public synchronized void func() {}` have an *intrinsic lock*, i.e. works like locking around the entire function body.
- **synchronized objects** `synchronized(obj) {}` have an *intrinsic lock* on the object for the code body.
- **static** methods TODO