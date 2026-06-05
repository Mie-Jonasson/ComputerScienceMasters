# Curriculum

All the slides and lectures are part of the syllabus. This includes the following topics (in bold the most common topics in the exam):

3D modelling:
- Parts and assemblies
- **Extrusion and revolution**
- **Symmetry and linear and circular patterns**
- Assemblies
- Drawings

3D printing:
- **Advantages and disadvantages**
- **Different 3D printing techniques: FDM, SLS, SLA**
- FDM basic settings: Layer height, infill, speed, support material, etc.

Flat sheet cutting:
- **Advantages and disadvantages**
- **Different flat sheet cutting techniques: Laser cutting, water jet, plasma cutting**
- Basic settings for laser cutting: Speed, power and frequency
- Techniques for flat sheets: finger joints, bending, etc.

Machine elements:
- Structural elements
- **DOF concept**
- **Linkages**
- **Plain and rolling bearings**
- **Linear guides**
- **Power transmission: Gears, pinion and rack, pinion and endless gear, lead screw and belts**

Electronics:
- **Voltage, current and resistance**
- **How to use a breadboard and a multimeter**
- **Ohm´s law and voltage dividers**
- **Diodes and LEDs, potentiometers, IR sensors, US sensors and switches: How they work, the circuits needed and how to wire them**
- **DC motors, stepper motors and servo motors: How they work, the circuits needed and how to wire them. Advantages and disadvantages of each of them.**
- **Transistors and H-bridge circuits**
- Voltage regulators and DC/DC converters

Microcontrollers:
- Arduino and microcontrollers
- **Reading sensors with a microcontroller: Circuits and programming**
- **Using actuators with a microcontroller: Circuits and programming**
- Digital communications: SPI and I2C

PCBs:
- **Advantages and disadvantages (compared to a breadboard)**
- Components of a PCB: pads, tracks, vias, etc
- Soldering

Milling and Turning:
- **Advantages and disadvantages**

Moulding and casting:
- **Advantages and disadvantages**
- **Moulding design and its properties**

# Study Plan

## Exam format

- ~15 min **group presentation** (all members present) + ~15 min **individual Q&A** per student
- Three question themes: **Q1 Manufacturing**, **Q2 How a machine works**, **Q3 Electronics**
- Q3 includes **practical wiring** on a breadboard — practice this; many students fail basic circuits
- Bring your **prototype** and a **smartphone** as a backup display

Study **bold curriculum topics** first, then cover the rest for breadth.

---

## Study progression

Work through these in order. Each step builds on the last; don't skip to electronics before you can explain your own prototype's mechanics.

### 1. Learn the theory (slides + bold topics)

- [ ] 3D modelling: extrusion, revolution, symmetry, patterns
- [ ] Manufacturing methods: 3D printing (FDM/SLS/SLA), flat-sheet cutting (laser/water jet/plasma), milling/turning, moulding — pros, cons, and when to use each
- [ ] Machine elements: DOF, linkages, bearings, linear guides, power transmission (gears, belts, lead screw, rack & pinion)
- [ ] Electronics fundamentals: voltage/current/resistance, Ohm's law, voltage dividers, breadboard, multimeter
- [ ] Components: switches, LEDs, potentiometers, IR/US sensors, diodes, DC/stepper/servo motors, transistors, H-bridge
- [ ] Microcontrollers: reading sensors, driving actuators, basic SPI/I2C
- [ ] PCBs: pros/cons vs breadboard, pads/tracks/vias, soldering basics

### 2. Practice Q1 — Manufacturing

For parts from your project, lecture slides, or exam examples, answer all three variants:

- [ ] Default: what process and material, and why?
- [ ] "What if it must be metal?"
- [ ] "What if you need 1000 units?"

Always justify with cost, time, tolerance, material properties, and surface finish.

### 3. Practice Q2 — How a machine works

Apply this sequence to your prototype and a few machines from the slides:

- [ ] Identify components: linear guides, bearings, motors, belts/gears/screws, structural elements
- [ ] Trace power: motor → reduction (if any) → end effector
- [ ] Count DOFs
- [ ] Name sensors and actuators — which type, and **why**?
- [ ] Identify driver (H-bridge, stepper driver) and microcontroller

### 4. Practice Q3 — Electronics

- [ ] Explain how to read a switch and a potentiometer (circuit + code)
- [ ] Explain how to control a DC motor (direction and speed) and how a servo works internally
- [ ] Wire from memory on breadboard or simulator: button, LED with resistor, potentiometer, DC motor via H-bridge, servo
- [ ] Draw schematics with correct symbols for every component used in the course
- [ ] Redo relevant MAs until wiring is automatic

### 5. Tie it together on your prototype

- [ ] For each part: manufacturing choice (Q1)
- [ ] Full mechanism walkthrough (Q2)
- [ ] Complete electronics schematic and wiring (Q3)
- [ ] Rehearse the group presentation; each member can answer "why did you choose X?"

### 6. Final check before the exam

- [ ] Prototype working (or ready to explain failures clearly)
- [ ] Can wire a button circuit on a breadboard without help
- [ ] Can justify every design and manufacturing decision on your project
- [ ] Smartphone charged; presentation parts assigned

# Notes