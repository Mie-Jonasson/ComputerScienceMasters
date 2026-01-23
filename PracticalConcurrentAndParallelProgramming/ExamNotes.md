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
- *Semaphores* allow threads up until capacity $c$ in the critical section. Reentrant locks, also called a *mutex*, are semaphores with $c = 1$, beware of faulty semaphores that may allow releasing locks that one does not hold, falsely increasing capacity.
- *Fairness* for different access types, i.e. in monitors Writer may wait forever if we allow new readers into the section while the write is still waiting. (starvation issue!)
- *Barriers* may be used to increase the chance of seeing possible concurrency errors, by ensuring all threads reach a certain point and the letting them all run wild.

## 3. **Visibility**: Explain the problems of visibility and reordering in shared memory concurrency. Motivate and describe the use of volatile variables and locks to tackle these problems. Show some examples of code from your solutions to the exercises in week 2.
- *Visibility*: CPUs are allowed to keep data (such as variable values) in registers / cache, that is then unavailable to other CPUs. The program stores data here, because it reduces latency for the thread to get and update the data.
    - flushing to main memory may be ensured using `lock`/`unlock` or `volatile` variables. This will make shared variables' updated value available across all CPUs.
- *Reordering*: the compiler may reorder instructions of the programme as to optimize performance. This may cause weird behavior, where critical sections are interleaved in an undesireable way.
    - using `synchronized` around two sections ensures that the steps of these sections are NOT interleaved with each other. One has the execute one section in full before executing the other section. 
    - `volatile` variables cannot be reordered but does not ensure mutual exclusion.

## 4. **Java memory model**: Motivate the need for the Java memory model. Explain the elements of the Java memory model including program order, happens-before order, synchronization order, and data races. Define what a correctly synchronized program is according to the Java memory model. Show some examples of code from your solutions to the exercises in week 3 and illustrate the use of the Java memory model to reason about their correctness.
- *Java Memory Model* describes *valid* executions of concurrent programs
    - Actions *thread(step)* are categorized as either *Variable Access* (accessing / updating program variables), *Synchronization* (locks, monitors, thread init / join) and *other*
    - *Program Order* defines the intra-thread order of execution for actions of a thread. For any thread, *a occurs before b according to program order* if a comes before b in the sequential execution of the thread body. Program order is a total order. Program order contains all pairs of ordered actions a, b 
    - *Happens-Before Order* defines relations between actions, stating *a happens-before b* if it is ordered by program order or other rules (f.ex. thread start)
    - *Synchronization Order* defines the total order of synchronization actions. A program may have multiple synchronization orders.
    - A *Well-formed execution* is an execution that is consistent with program order, happens-before order and synchronization order. The JVM always produces well-formed executions.
    - *Conflicting Actions* are all accesses to non-volatile variables. Conflicting Actions lead to *Data Races* if the actions are NOT ordered by Happens-Before.
- A *Correctly Synchronized Program* according to the Java Memory Model is a program where none of its executions contain data races, i.e. all conflicting actions are ordered by Happens-Before.

## 5. **Thread-safe classes**: Define and explain what makes a class thread-safe. Explain the issues that may make classes not thread-safe. Show some examples of code from your solutions to the exercises in week 4.
- *Thread-Safe Classes* is useful, as analyzing a huge code base is infeasible - but reasoning about thread-safety of a class is feasible and may then be generalized for all usage of the class.
    - *Formal Definition*: A class is thread-safe if NO concurrent executions contain data races on the fields of the class (i.e. method calls & direct field accesses)
    - We should consider the following to argue a class as thread safe.
        - *Class state*: methods should only manipulate the class state and should not take object references as arguments (such as lists)
        - *Escaping*: variables should be private so threads do not "escape" the locking/synchronization when updating - also, never return a reference to complex private class variables.
        - *Safe Publication*: ensure objects are initialized properly, avoiding visibility issues. Make class variables `volatile`, `static`, `final` (if never modified), use Atomic Type Class or initialize to default value.
        - *Immutability*: Immutable classes are thread-safe if we ensure they cannot be modified after initialization and have safe publication.
        - *Mutual Exclusion*: Accesses to mutable state should be ensured mutually exclusive. (if NOT Immutable)
- *Instance Confinement*: encapsulating non-thread-safe classes into a thread-safe capsule class. In Java, the types `synchronized<type>` is an instance confinement that is defined in many cases.
- *Extension in Thread-Safe Classes*: may be done by acquiring intrinsic lock on the class instance or by adding the method to the thread-safe class.

## 6. **Testing**: Explain the challenges in ensuring the correctness of concurrent programs. Describe different testing strategies for concurrent programs, and their advantages and disadvantages. Show some examples of code from your solutions to the exercises in week 5.
- Easy to show bugs exist - hard to prove the absence! We can make tests to test *properties* of a *specification*, to convince ourselves that at least certain properties hold.
    - *Safety* properties are about avoiding "bad"/unintended behavior. Has a *finite* counterexample where the property does not hold (interleaving is allowed to be infinite, but the part used to prove the counterexample should be finite).
    - *Liveness* properties are about ensuring "good"/intended behavior happens eventually. Has an *infinite* counterexample where the property never holds.
- *Functional Correctness Testing* is about finding *counterexamples* to intended behavior, and sometimes need to be run many times to catch an unlikely but possible *unintended interleaving*.
    - Use of *Barriers* to increase thread contention may increase likelihood of finding failing interleavings.
    - Make *Parametrized Tests* to try many different inputs for convincing of robustness.
    - Make a *Repeated Test* to run multiple times trying to trigger the failing interleavings.
- Some things are impossible to test; rely on *Formal Verification* in terms of mathematical proofs of the programme working as intended.

## 7. **Performance measurements**: Motivate and explain how to measure the performance of Java code. Illustrate some of the pitfalls there are in doing such measurements. Show some examples of code from your solutions to the exercises in week 9.
- Making things run faster without quantifying is only half the fun - being able to numerically compare different versions in terms of runtime and scalability is super important!
    - For example; thread creation is expensive, investigate how many threads it "pays off" to do on a given computer.
- We usually refer to performance measurement and comparison as *benchmarking*. We use a library to do this.
    - Be aware that performance varies all the time - and depends on hardware and background processes.
    - We run the experiment many times and report average runtime as well as standard deviation.
    - We can make a generalized class running the marking for us many-many times and reporting the runtime - just pass a lambda function that it should call and benchmark!
- TODO: Review more!!!

## 8. **Performance and Scalability**: Explain how to increase the performance of Java code exploiting concurrency. Illustrate some of the pitfalls there are in doing this. Show some examples of code from your solutions to the exercises in week 10.
- We can increase performance by dividing a task into smaller tasks and executing concurrently - but *how* do we *divide* the tasks? *How many threads* can we make without the overhead of creating threads becomes a problem?
    - Split into small enough but not too small subsets - possibly using a *threshold* on subset size.
    - Minimize unused threads in pool. Minimize thread contention.
    - Lock striping where instead of a single lock for an entire collection, a lock for one or few parts of the collection - better distributed and avoids threads always waiting for each other.
- Can assign *many tasks* to a *single thread* (i.e. *threadpools* where we submit work and work is taken on by an available thread in the pool)
    - *ForkJoinPool* are the ones we hav eused - many other exist. Gist of an *ExecutorService* is the ability to submit task and the executor will assign tasks to threads when available.
    - We call *pool.shutdown()* once no more tasks need to be submitted. Then we *awaitTermination(100, TimeUnit.seconds)* to wait up to 100 seconds for the remaining tasks to finish.
- *Amdahl's Law* describes the speed-up that can be obtained from concurrency. Takes the fraction of the problem that can be executed concurrently and the number of threads.
    - *Max Speed-Up* TODO

## 9. **Lock-free Data Structures**: Define and motivate lock-free data structures. Explain how *compare-and-swap* (CAS) operations can be used to solve concurrency problems. Show some examples of code from your solutions to the exercises in week 6.
- *Lock-free Data Structures* is used to describe objects that are safe to use in concurrent programs but that do not utilize locks.
    - Operations are *Non-blocking* in lock-free data structure, but may instead incur starvation. *"trying again until it succeeds"*
    - Nested levels of non-blocking: *Obstruction-Free* (If the thread executes in isolation, it will finish in a finite number of steps), *Lock-Free* (If some thread will finish in a finite number of steps), *Wait-Free* (all threads will finish in a finite number of steps)
    - A *Con* of lock free data structures is *increased memory overhead*.
- The most prominent lock-free data structure design pattern is *Compare-And-Swap* (CAS). This is a conditional setting of a register in a single operation, putting value b into the register if the current register == a.
```java
do {
    old_value = v.get()
    new_value = old_value ???
} while (!v.compareAndSet(old_value, new_value))
```

## 10. **Linearizability**: Explain and motivate linearizability. Explain how linearizability can be applied to reason about the correctness of concurrent objects. Show some examples of code in your solutions to the exercises in week 7 where you used linearizability to reason about correctness.
- *Linearizability* is about using sequential specifications to argue about concurrent executions. I.e. we want the concurrent behavior of the code to behave as-if it was executed sequentially.
- *Sequential Consistency* refers to methods calls appearing to happen one-at-a-time and that method calls should appear to take effect in program order. 
    - Concurrent executions are sequentially consistent if there exists at least 1 re-ordering of operations that is (1) one-at-a-time (2) thread program order is retained and (3) execution satisfies specification of the object.
- *Linearizability* extends Sequential Consistency to also require real-time order preserved. "Each method should take effect at some instant between invocation and response". We define this instant as the *linearization point*
- A *concurrent object* is *linearizable* iff all concurrent executions of method calls are linearizable - we do this by selection *linearization points* in the source code.

## 11. **Streams**: Explain and motivate the use of streams to parallelize computation. Discuss issues that arise in operations executed by parallel streams. Show some examples of code from your solutions to the exercises in week 11.
- If we are applying *multiple transformations / filterings* to an *input stream* (such as words, list of integers or transfers etc.) we can consider it similarly to how we do in Functional Programming.
- We define a *pipeline* from input to output of various transformations, we can represent this as a Java *Stream*.
    - Streams are easy to parallelize; `<stream_object>.parallel().<transformations>`
    - Streams do not store intermediate states in temporary variables
    - Streams are *lazily evaluated*
- There are three main types of stream elements; *sources* (initial constructors of a stream), *intermediate operations* (filtering and transformations) & *terminal operations* (finalizing the stream to an output state)
    - Source Examples: `Arrays.stream(arr)`, `Stream.of(1, 2, 3, 4)`
    - Operation Examples: `filter(x -> bool)` (filters when lambda is false), `map(x -> y)`, `limit(n)` (only first n elements), `skip(n)` (skip n elements), `distinct()` (removes duplicated elements), `sorted()`
    - Terminal Examples: `min()`, `max()`, `sum()`, `average()`, `count()`, `forEach(x -> void)`(`forEach(System.out::println)`, can be replaced with `forEachOrdered` if order of stream is important), `reduce(acc, (acc, elem)-> new_acc)` (like folding)

## 12. **Message Passing**: Explain and motivate the actor model of concurrent computation. Discuss advantages and disadvantages of approaches to distribute computation in actor systems. Show some examples of code from your solutions to the exercises in week 12 and 13.
- Instead of having shared memory, we can utilize *message passing* where each actor is only required to keep track of local state and keep track of that based on messages received.
- Messages are always strings, so we represent class objects as *json*, that is packaged and unpackaged by the sender and receiver.
- The *Actor Model* contains individual actors (f.ex. threads) that communicate with each other and do not share memory - they each have their own *local state* and *mailbox*.
    - The mailbox is usually a FIFO queue, and we cannot guarantee that messages are received in the same order they are sent.
    - Actors can (1) receive messages, (2) send messages, (3) create new actors & (4) update their internal state
    - Sending is *non-blocking*, receiving is *blocking* when the mailbox is empty (i.e. awaiting message to process)
- In Erlang:
    - each file corresponds to an actor
    - Init / start functions are usually public for us to be able to interact with the actor
    - Records used to define the internal state, loop is the main function (recursive definition) waiting to receive messages and processing each type as they arrive.
- We may distribute computations in an actor system by having an actor spawn *workers* that do "the work" while the actor itself is a middle-man managing receiving requests, distributing them and passing back the answers.
    - This is called *dynamic topology* as the number of workers may vary over the lifetime of an execution, and may scale according to workload requests. (*load balancing*) 
    - In particular, it also allows *fault tolerance* as we may boot up a new worker when a worker fails, and always retain some number of active workers.
    - Workers may shut down with an error or shut down *normally* (i.e. because we told it to) *let it crash!* model using *process monitoring*

# Code Examples
## Question 1
Run from `Assignment1/Exercise1/week01exercises/` the command `gradle run -PmainClass=exercises01.CounterThreads2Covid`
```java
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
Run from `Assignment1/Exercise2/week02exercises/` the command `gradle run -PmainClass=exercises02.ReadersWriters`
```java
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
Run from `Assignment1/Exercise2/week02exercises/` the command `gradle run -PmainClass=exercises02.TestMutableInteger`
```java
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
    private volatile int value = 0; // made volatile to make sure it is flushed when updated
    public void set(int value) { // might have synchronized these two methods instead
        this.value = value;
    }
    public int get() {
        return value;
    }
}
```

## Question 4
Run from `Assignment2/Exercise3/week03exercises/` the command `gradle run -PmainClass=exercises03.CountingThreads`
```java
import java.util.concurrent.locks.ReentrantLock;

public class CountingThreads {
    int count;
    ReentrantLock l;

    public CountingThreads() throws InterruptedException {
        count = 0; // (init(c)) - variable access
        l = new ReentrantLock(); // (init(l)) - variable access
        
        CountingThread t1 = new CountingThread(); // (init(t1))
        CountingThread t2 = new CountingThread(); // (init(t2))
        
        t1.start(); // (start(t1)) - synchronization
        t2.start(); // (start(t2)) - synchronization

        t1.join(); // (join(t1)) - synchronization
        t2.join(); // (join(t2)) - synchronization
        
        System.out.println("count="+count); // (3) - variable access
    }

    public class CountingThread extends Thread {
        public void run() {
            l.lock(); // (4) - synchronization
            int temp = count; // (1) - variable access
            count = temp + 1; // (2) - variable access
            l.unlock(); // (5) - synchronization
        }
    }


    public static void main(String[] args) throws InterruptedException {
        new CountingThreads();
    }
}
```
### Happens-Before Order
$HB ^m_{po}=$ m(init(c)) -> m(init(l)) -> m(init(t1)) -> m(init(t2)) -> m(start(t1)) -> m(start(t2)) -> m(join(t1)) -> m(join(t2)) -> m(3)

$HB ^{t1}_{po}=$ t1(4) -> t1(1) -> t1(2) -> t1(5)

$HB ^{t2}_{po}=$ t2(4) -> t2(1) -> t2(2) -> t2(5)

$HB_{init}=$ {m(start(t1)) -> t1(4), m(start(t2)) -> t2(4)}

$HB_{ter}=$ {t1(5) -> m(join(t1)), t2(5) -> m(join(t2))}

### Synchronization Orders
m(start(t1)), m(start(t2)), t1(4), t1(5), t2(4), t2(5), m(join(t1)), m(join(t2))
m(start(t1)), t1(4), m(start(t2)), t1(5), t2(4), t2(5), m(join(t1)), m(join(t2))
m(start(t1)), t1(4), t1(5), m(start(t2)), t2(4), t2(5), m(join(t1)), m(join(t2))
m(start(t1)), m(start(t2)), t2(4), t2(5), t1(4), t1(5), m(join(t1)), m(join(t2))

## Question 5
Run from `Assignment2/Exercise4/week04exercises/` the command `gradle run -PmainClass=exercises04.PersonTester`
```java
package exercises04;

public class Person {                                                           // all variables are private
  private static long currentId;                                                // internal class-state, never exposed
  private static boolean firstPersonInitialized = false;                        // internal class-state, never exposed
  private final long id;                                                        // immutable
  private final String name;                                                    // immutable
  private int zip;                                                              // init default
  private String address;                                                       // init default

  public Person() {                                                             // default constructor
    this(0);
  }

  public Person(long startId) {                                                 // constructor with specific start-id
    synchronized (Person.class) {
      if (!firstPersonInitialized) {
        currentId = startId;
        firstPersonInitialized = true;
      }
      id = currentId;
      name = "John Doe";
      currentId++;
    }
  }

  public synchronized void changeAddress(String address, int zip) {             // mutable fields, update
    this.zip = zip;
    this.address = address;
  }

  public long getId() {                                                         // immutable field, no lock
    return id;
  }

  public String getName() {                                                     // immutable field in our implementation, no lock
    return name;
  }

  public synchronized int getZip() {                                            // mutable field, read, simple type
    return zip;
  }

  public synchronized String getAddress() {                                     // mutable field, read, strings are practically immutable
    return address;
  }
}

```

## Question 6
Run from `Assignment3/Exercise5/week05exercises/` the command `gradle cleanTest test --tests exercises05.ConcurrentSetTest`
```java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Disabled;
import java.util.Random;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.atomic.AtomicInteger;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.concurrent.BrokenBarrierException;

public class ConcurrentSetTest {

    // Variable with set under test
    private ConcurrentIntegerSet set;

    // Uncomment the appropriate line below to choose the class to test
    @BeforeEach
    public void initialize() {
        // init set
        // set = new ConcurrentIntegerSetBuggy(); // for 5.1.1, 5.1.2
        // set = new ConcurrentIntegerSetSync(); // for 5.1.3
        set = new ConcurrentIntegerSetLibrary(); // for 5.1.4
    }

    // @Disabled
    @RepeatedTest(10000)
    @DisplayName("Adding Single element to Set")
    public void addSingle() throws InterruptedException {
        int nrThreads = 32;
        Random r = new Random();
        int e = r.nextInt();

        AtomicInteger trueCount = new AtomicInteger();

        CyclicBarrier barrier = new CyclicBarrier(nrThreads+1);

        for (int i = 0; i < nrThreads; i++) {
            new Thread(() -> {
                try {
                    barrier.await();
                    boolean s = set.add(e);
                    trueCount.getAndAdd(s ? 1 : 0);
                    barrier.await();
                } catch (InterruptedException | BrokenBarrierException exc ) {
                    exc.printStackTrace();
                }
            }).start();
        }

        try {
            barrier.await();
            barrier.await();
        } catch (InterruptedException | BrokenBarrierException exc ) {
            exc.printStackTrace();
        }

        assertEquals(set.size(), 1);
        assertEquals(trueCount.get(), 1);
    }

    @RepeatedTest(10000)
    @DisplayName("Remove Single element from Set")
    public void removeSingle() throws InterruptedException {
        int nrThreads = 32;
        Random r = new Random();
        int e = r.nextInt();
        set.add(e);

        AtomicInteger trueCount = new AtomicInteger();

        CyclicBarrier barrier = new CyclicBarrier(nrThreads+1);

        for (int i = 0; i < nrThreads; i++) {
            new Thread(() -> {
                try {
                    barrier.await();
                    boolean s = set.remove(e);
                    trueCount.getAndAdd(s ? 1 : 0);
                    barrier.await();
                } catch (InterruptedException | BrokenBarrierException exc ) {
                    exc.printStackTrace();
                }
            }).start();
        }

        try {
            barrier.await();
            barrier.await();
        } catch (InterruptedException | BrokenBarrierException exc ) {
            exc.printStackTrace();
        }

        assertEquals(0, set.size());
        assertEquals(1, trueCount.get());
    }
}
```

## Question 7
Run from `Assignment4/Exercise9/week09exercises/` the command `gradle run -PmainClass=exercises09.TestCountPrimesThreads`
```java
import benchmarking.Benchmark;
import benchmarking.Benchmarkable;

public class TestCountPrimesThreads {

  public static void main(String[] args) { new TestCountPrimesThreads(); }

  public TestCountPrimesThreads() {
    Benchmark.SystemInfo();
    final int range= 100_000;
    Benchmark.Mark7("countSequential", i -> countSequential(range));
    for (int c= 1; c<=32; c++) {
      final int threadCount = c;
      Benchmark.Mark7(String.format("countParallelN %7d", threadCount), 
            i -> countParallelN(range, threadCount));
    }
  }

  private static boolean isPrime(int n) {
    int k = 2;
    while (k * k <= n && n % k != 0)
      k++;
    return n >= 2 && k * k > n;
  }

  // Sequential solution
  private static int countSequential(int range) {
    int count= 0;
    final int from= 0, to= range;
    for (int i= from; i<to; i++)
      if (isPrime(i)) count++;
    return count;
  }

  // General parallel solution, using multiple threads
  private static int countParallelN(int range, int threadCount) {
    final int perThread= range / threadCount;
    final PrimeCounter lc= new PrimeCounter();
    Thread[] threads= new Thread[threadCount];
    for (int t= 0; t<threadCount; t++) {
        final int from= perThread * t, 
        to = (t+1==threadCount) ? range : perThread * (t+1); 
        threads[t]= new Thread( () -> {
          for (int i= from; i<to; i++)
            if (isPrime(i)) lc.increment();
        });
    }
    for (int t= 0; t<threadCount; t++) 
      threads[t].start();
    try {
      for (int t=0; t<threadCount; t++) 
        threads[t].join();
        //System.out.println("Primes: "+lc.get());
    } catch (InterruptedException exn) { }
    return lc.get();
  }
}
```

```
# OS:   Mac OS X; 14.6; aarch64
# JVM:  Homebrew; 17.0.16
# CPU:  null; 8 "cores"
# Date: 2025-10-27T11:10:50+0100
countSequential                 2011099,6 ns   12439,42        128
countParallelN       1          2068329,6 ns     835,60        128
countParallelN       2          1364334,1 ns    4115,08        256
countParallelN       3          1162648,4 ns   16703,89        256
countParallelN       4          1030419,1 ns   24443,32        256
countParallelN       5          1187034,4 ns   15321,28        256
countParallelN       6          1205606,4 ns   17529,10        256
countParallelN       7          1209973,6 ns    3557,38        256
countParallelN       8          1218157,1 ns    8090,17        256
countParallelN       9          1230767,1 ns   13472,11        256
countParallelN      10          1241062,6 ns   19223,15        256
countParallelN      11          1264616,0 ns   72561,72        256
countParallelN      12          1245896,4 ns    5645,03        256
countParallelN      13          1260012,1 ns   16850,05        256
countParallelN      14          1263548,3 ns   16980,37        256
countParallelN      15          1269679,4 ns    7821,83        256
countParallelN      16          1276054,0 ns    7158,31        256
countParallelN      17          1287015,6 ns   17319,76        256
countParallelN      18          1291994,7 ns   16053,21        256
countParallelN      19          1293192,1 ns    4855,54        256
countParallelN      20          1301440,3 ns   13505,66        256
countParallelN      21          1309524,4 ns   13209,46        256
countParallelN      22          1305114,8 ns    5211,67        256
countParallelN      23          1303006,5 ns   13335,20        256
countParallelN      24          1283544,2 ns   17032,02        256
countParallelN      25          1238257,4 ns   17993,29        256
countParallelN      26          1211900,4 ns   17041,52        256
countParallelN      27          1200906,8 ns   20362,14        256
countParallelN      28          1188079,8 ns   15213,46        256
countParallelN      29          1184386,4 ns   19187,64        256
countParallelN      30          1184670,5 ns   22376,67        256
countParallelN      31          1183717,0 ns    8540,14        256
countParallelN      32          1186879,6 ns    7459,68        256

```

## Question 8
Run from `Assignment5/Exercise10/week10exercises/` the command `gradle run -PmainClass=exercises10.TestCountPrimesThreads`
```java
import java.util.ArrayList;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicLong;

import benchmarking.Benchmark;

public class TestCountPrimesThreads {
    public static void main(String[] args) {
        new TestCountPrimesThreads();
    }

    public TestCountPrimesThreads() {
        final int range = 100_000;
        Benchmark.Mark7("countSequential", i -> countSequential(range));
        for (int c = 1; c <= 16; c = 2 * c) {
            final int threadCount = c;
            Benchmark.Mark7(String.format("countParallelN %2d", threadCount),
                    i -> countParallelN(range, threadCount));
            Benchmark.Mark7(String.format("countParallelNLocal %2d", threadCount),
                    i -> countParallelNLocal(range, threadCount));
            Benchmark.Mark7(String.format("countParallelNExecutors %2d", threadCount),
                    i -> countParallelNExecutors(range, threadCount));
        }
    }

    private static boolean isPrime(int n) {
        int k = 2;
        while (k * k <= n && n % k != 0)
            k++;
        return n >= 2 && k * k > n;
    }

    // Sequential solution
    private static long countSequential(int range) {
        long count = 0;
        final int from = 0, to = range;
        for (int i = from; i < to; i++)
            if (isPrime(i))
                count++;
        return count;
    }

    // General parallel solution, using multiple threads
    private static long countParallelN(int range, int threadCount) {
        ...
    }

    // General parallel solution, using multiple threads
    private static long countParallelNLocal(int range, int threadCount) {
        ...
    }

    private static class countPrimesTask implements Callable<Integer> {
        private final int low, high;

        countPrimesTask(int l, int h) {
            low = l;
            high = h;
        }

        @Override
        public Integer call() {
            Integer count = 0;
            for (int i = low; i < high; i++) {
                if (isPrime(i))
                    count++;
            }
            return count;
        }
    }

    private static long countParallelNExecutors(int range, int threadCount) {
        final int perThread = range / threadCount;
        final ArrayList<Future<Integer>> results = new ArrayList<Future<Integer>>();

        ExecutorService pool = new ForkJoinPool(4);

        for (int t = 0; t < threadCount; t++) {
            final int from = perThread * t,
                    to = (t + 1 == threadCount) ? range : perThread * (t + 1);
            final int threadNo = t;
            Future<Integer> f = pool.submit(new countPrimesTask(from, to));
            results.add(f);
        }

        pool.shutdown();

        long count = 0;
        for (Future<Integer> j : results) {
            try {
                count += j.get().intValue();
            } catch (InterruptedException | ExecutionException e) {
            }
        }

        try {
            // Wait for all tasks to complete or timeout after 100 seconds
            if (pool.awaitTermination(1, TimeUnit.SECONDS)) {
                // System.out.println("All tasks completed successfully.");
            } else {
                System.out.println("Timeout elapsed before termination.");
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return count;
    }
}
```

```
countSequential                 5408642.5 ns  337710.19         64
countParallelN  1               5461181.3 ns  298241.84         64
countParallelNLocal  1          5518456.8 ns  337170.10         64
countParallelNExecutors  1       5416058.0 ns  253290.92         64
countParallelN  2               3604433.4 ns  174302.17        128
countParallelNLocal  2          3633222.5 ns  154604.32        128
countParallelNExecutors  2       3759861.8 ns  287296.58        128
countParallelN  4               2818494.9 ns  199681.20        128
countParallelNLocal  4          2606914.7 ns   82854.02        128
countParallelNExecutors  4       2947275.3 ns  104202.56        128
countParallelN  8               2583905.5 ns  264871.43        128
countParallelNLocal  8          2419737.9 ns  204061.19        128
countParallelNExecutors  8       2624033.0 ns  197332.33        128
countParallelN 16               2744961.6 ns  301596.23        128
countParallelNLocal 16          2590706.1 ns  193211.93        128
countParallelNExecutors 16       2690385.7 ns  418394.89        128
```

## Question 9
Run from `Assignment3/Exercise6/week06exercises/` the command `gradle run -PmainClass=exercises06.CasHistogram`
```java
import java.util.concurrent.atomic.AtomicInteger;

class CasHistogram implements Histogram {
  private final AtomicInteger[] counts;

  public CasHistogram(int span) {
    counts = new AtomicInteger[span];
    for (int i = 0; i < span; i++) {
      counts[i] = new AtomicInteger();
    }
  }

  public int getCount(int bin) {
    return counts[bin].get();
  }

  public int getSpan() {
    return counts.length;
  }

  public void increment(int bin) {
    int val;
    do {
      val = counts[bin].get();
    } while (!counts[bin].compareAndSet(val, val + 1));
  }

  public int getAndClear(int bin) {
    int val;
    do {
      val = counts[bin].get();
    } while (!counts[bin].compareAndSet(val, 0));
    return val;
  }
}

```

## Question 10
```java
class LockFreeStack<T> {
    AtomicReference<Node<T>> top = new AtomicReference<Node<T>>(); // Initializes to null

    public void push(T value) {
        Node<T> newHead = new Node<T>(value);           // Pu1
        Node<T> oldHead;                                // Pu2
        do {
            oldHead      = top.get();                   // Pu3
            newHead.next = oldHead;                     // Pu4
        } while (!top.compareAndSet(oldHead,newHead));  // Pu5 - Linearization point for method

    }

    public T pop() {
        Node<T> newHead;                                // Po1
        Node<T> oldHead;                                // Po2
        do {
            oldHead = top.get();                        // Po3 - Linearization point if stack is empty
            if(oldHead == null) { return null; }        // Po4
            newHead = oldHead.next;                     // Po5
        } while (!top.compareAndSet(oldHead,newHead));  // Po6 - Linearization point for method if
                                                        //       stack is non-empty

        return oldHead.value;
    }
}
```

For the `push()` method of `LockFreeStack` there is only a single linearization point which is
`Pu5` as labeled above, which is where the item is inserted into the stack by swapping the old head
for the new head.

For the `pop()` method of `LockFreeStack` there are two linearization points. One at Po3, which
is the linearization point if the stack is empty. And at Po6 if the stack is non-empty, which is
where the item is removed from the stack by swapping the old head for the new one.

**Correctness**:
If two threads execute push at the same time, only one will succeed at executing `Pu5`, while the
other one fails and retries. The same argument can be made for two threads executing pop at the
same time, where one will fail at `Po6` and retry.
Similarly the same thing happens if one thread executes push while another executes pop. One thread
will succeed in changing the head of the stack, while the other will fail and retry.

## Question 11
Run from `Assignment5/Exercise11/week11exercises/` the command `gradle run -PmainClass=exercises11.PrimeCountingPerf`
```java
import java.util.*;
import java.util.stream.*;
import java.io.IOException;
import java.lang.NumberFormatException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.concurrent.atomic.AtomicLong;
import benchmarking.Benchmark;

class PrimeCountingPerf { 
  public static void main(String[] args) { new PrimeCountingPerf(); }
  static final int range= 100000;

  //Test whether n is a prime number
  private static boolean isPrime(int n) {
    int k= 2;
    while (k * k <= n && n % k != 0)
      k++;
    return n >= 2 && k * k > n;
  }

  // Sequential solution
  private static long countSequential(int range) {
    long count = 0;
    final int from = 0, to = range;
    for (int i=from; i<to; i++)
      if (isPrime(i)) count++;
    return count;
  }

  // IntStream solution
  private static long countIntStream(int range) {
    return IntStream.range(2, range)
      .filter(i -> isPrime(i))
      .count();
  }

  // Parallel Stream solution
  private static long countParallel(int range) {
    return IntStream.range(2, range)
      .parallel()
      .filter(i -> isPrime(i))
      .count();
  }

// parallelStream solution
  private static long countparallelStream(List<Integer> list) {
    return list
      .parallelStream()
      .filter(i -> isPrime(i))
      .count();
  }

  public PrimeCountingPerf() {
    Benchmark.Mark7("Sequential", i -> countSequential(range));

    Benchmark.Mark7("IntStream", i -> countIntStream(range));
    
    Benchmark.Mark7("Parallel", i -> countParallel(range));

    List<Integer> list = new ArrayList<Integer>();
    for (int i= 2; i< range; i++){ list.add(i); }
    Benchmark.Mark7("ParallelStream", i -> countparallelStream(list));
  }
}
```

```
Sequential                      1986799,4 ns   11162,72        128
IntStream                       2011782,4 ns   17478,71        128
Parallel                         529728,2 ns    3814,19        512
ParallelStream                   524621,2 ns    5687,18        512
```

## Question 12
```erlang
% raup@itu.dk * 2024-11-22

-module(server).
% to be extended
-export([start/2, init/2]).
-include("defs.hrl").

% 1. State

-record(server_state, {
    idle_list = [], pending_tasks = [], total_workers = 0, min_workers, max_workers
}).

% 2. Start

start(MinNumWorkers, MaxNumWorkers) ->
    spawn(?MODULE, init, [MinNumWorkers, MaxNumWorkers]).

% 3. Initialization

init(MinNumWorkers, MaxNumWorkers) ->
    State = #server_state{min_workers = MinNumWorkers, max_workers = MaxNumWorkers},
    NewState = spawn_n_workers(State#server_state.min_workers, State),
    loop(NewState).

% 4. Behavior upon receiving messages

loop(State) ->
    receive
        {work_done, WorkerPID} ->
            handle_work_done(WorkerPID, State);
        {compute, SenderPID, Tasks} ->
            handle_compute(SenderPID, Tasks, State);
        idle_workers ->
            io:format("Idle workers: ~p~n", [State#server_state.idle_list]);
        {'DOWN', _, _, _, normal} ->
            handle_normal(State);
        {'DOWN', _, _, PID, Reason} ->
            handle_error(PID, Reason, State)
    end.

% 5. Message handlers

handle_normal(State) ->
    loop(State).

handle_error(PID, Reason, State) ->
    io:format("Worker ~w crashed with error ~p~n", [PID, Reason]),
    NewState = spawn_n_workers(1, State#server_state{
        total_workers = State#server_state.total_workers - 1
    }),
    loop(NewState).

handle_compute(_, [], State) ->
    loop(State);
handle_compute(
    SenderPID,
    [Task | Remaining],
    State = #server_state{
        total_workers = TotalWorkers, max_workers = MaxWorkers, idle_list = IdleList
    }
) ->
    case IdleList of
        [] ->
            case TotalWorkers < MaxWorkers of
                false ->
                    NewState = State#server_state{
                        pending_tasks = [{Task, SenderPID} | State#server_state.pending_tasks]
                    };
                true ->
                    NewState = spawn_n_workers(1, State),
                    handle_compute(SenderPID, [Task | Remaining], NewState)
            end;
        [WorkerPID | RemainingWorkers] ->
            WorkerPID ! {compute, SenderPID, Task},
            NewState = State#server_state{idle_list = RemainingWorkers}
    end,
    handle_compute(SenderPID, Remaining, NewState).

handle_work_done(
    WorkerPID,
    State = #server_state{
        total_workers = TotalWorkers, min_workers = MinWorkers, idle_list = IdleList
    }
) ->
    case State#server_state.pending_tasks of
        [] ->
            case TotalWorkers > MinWorkers of
                false ->
                    NewState = State#server_state{idle_list = [WorkerPID | IdleList]};
                true ->
                    WorkerPID ! stop,
                    NewState = State#server_state{total_workers = TotalWorkers - 1}
            end;
        [{Task, SenderPID} | Remaining] ->
            WorkerPID ! {compute, SenderPID, Task},
            NewState = State#server_state{pending_tasks = Remaining}
    end,
    loop(NewState).

% Private functions (to be used, e.g., by message handlers)

spawn_n_workers(0, State) ->
    State;
spawn_n_workers(NumWorkers, State) ->
    PID = worker:start(self()),
    monitor(process, PID),
    NewState = State#server_state{
        idle_list = [PID | State#server_state.idle_list],
        total_workers = State#server_state.total_workers + 1
    },
    spawn_n_workers(NumWorkers - 1, NewState).


```

# General Notes
## Abstract Syntaxes
### Interleaving
\<thread>(\<step>), \<thread>(\<step>), ...

## Java Modifiers
- **Synchronized methods** `public synchronized void func() {}` have an *intrinsic lock*, i.e. works like locking around the entire function body.
- **synchronized objects** `synchronized(obj) {}` have an *intrinsic lock* on the object for the code body.
- **static** methods TODO
- **static** variables TODO
- **final** variables are non-modifiable variables.
- **volatile** variables ensure visibility (flushing to shared memory) and prevents reordering (but does not ensure mutual exclusion)
- **Future<\type>** refers to a callable returning a certain type, which may be used as return type for tasks submitted to threadpools