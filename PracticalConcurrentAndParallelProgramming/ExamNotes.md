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
- *Semaphores* allow threads up until capacity $c$ in the critical section. Reentrant locks, also calles a *mutex*, are semaphores with $c = 1$, beware of faulty semaphores that may allow releasing locks that one does not hold, falsely increasing capacity.
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
- TODO

## 8. **Performance and Scalability**: Explain how to increase the performance of Java code exploiting concurrency. Illustrate some of the pitfalls there are in doing this. Show some examples of code from your solutions to the exercises in week 10.
- TODO

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
- TODO

## 12. **Message Passing**: Explain and motivate the actor model of concurrent computation. Discuss advantages and disadvantages of approaches to distribute computation in actor systems. Show some examples of code from your solutions to the exercises in week 12 and 13.
- TODO

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
Run from `Assignment3/Exercise5/week05exercises/` the command `radle cleanTest test --tests exercises05.ConcurrentSetTest`
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
```java
```

## Question 8
```java
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
```java
```

## Question 12
```erlang
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