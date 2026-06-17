# Exam Question Notes

**Format:** 15 min group presentation → per student ~15 min Q&A on **Q1 Manufacturing**, **Q2 How a machine works**, **Q3 Electronics**. Bring prototype + phone. Q3 may include **live breadboard wiring**.

---

## Q1 — How would you manufacture these parts?

*Slides also ask: "And if you need to make it of metal?" / "And if you need 1000 parts?"*

### Approach (memorize)
1. **Identify** geometry clues → process (ribs/bosses/ejector marks = injection mould; layers = FDM; finger joints = laser cut; axisymmetric = turning)
2. **Default:** prototype process + material (usually FDM/PLA or laser-cut MDF/acrylic)
3. **Justify** with: **cost, time, tolerance, material properties, surface finish**
4. **Metal variant:** CNC mill, die cast, sheet metal (cut + bend), turning — match geometry
5. **1000 units:** injection moulding (plastic) or die cast/CNC at scale — mould cost amortised

### Practice images (`all_parts/`)

**Part 02**
![](Exam%20Questions%20Spring%202026/all_parts/12019-1.jpg)
*Your answer:*
1. It is some kind of plastic structure with multiple slots for mounting things, and with a mesh pattern inside the hollow side of the part for strength.
2. For initial prototyping, I would choose to 3D print this using FDM.
3. I would pick this approach initially as it is cheap, easily accessible and has a low lead time from idea -> design -> physical part. It suffers from anisotropy and needing support, but in a prototyping phase we can live with these limitations.
4. For this part, milling and drilling would probably be the main way forward, as the part is 3-dimensional in a way hard to model using flat sheets og revolution parts.
5. This part looks injection moulded (see date-stamp and ejection marks), which is also the approach i would pick for mass-manufacturing, where the cost of creating a good mould for the part will be minor in the unit-cost for mass manufacturing.

**Part 04**
![](Exam%20Questions%20Spring%202026/all_parts/201904220001.jpg)
*Your answer:*
1. This is an injection mold. We can visibly see the sprues and how the parts have symmetric outlines on either part. The mould is made of metal and has corner rods for ensuring the two parts of the mould are properly aligned.
2. Per default, I would produce it using milling.
3. I would pick this option as it give a smooth finish on all edges, with the quality of the mould being highly related to the quality of the injection moulded products. Since we also only need a few or a single one, the "slowness" of creating the mould would not be a prominent issue.
4. It is already.
5. I do not think mass producing this mould is as relevant, but of course creating this mould in the first place only makes sense if we need a lot of identical parts manufactured.

**Part 05**
![](Exam%20Questions%20Spring%202026/all_parts/legos-hero.png)
*Your answer:*
1. These are lego bricks. They are used to stack on top of each other and build 3D structures.
2. If I had to initially develop the shape i would likely go for 3D printing using FDM.
3. I would initially pick this due to accesibillity and price as well as the quick iterations over the design that are possible. I do note that a single or few lego bricks do not make a lot of sense, so switching to injection moulding rather quickly may pay off (most lego sets are at least a couple hundred bricks).
4. I do not think that is relevant for this bit.
5. Injection Moulding would be the way to go in this case, and maybe even for smaller scale productions (as you would always need a bunch of lego bricks to play around!)

**Part 07**
![](Exam%20Questions%20Spring%202026/all_parts/78-hajlitott-lemezalkatresz.JPG)
*Your answer:*
1. This is a bending metal piece with two mounting holes perpendicular to the main surface.
2. I would go for flat sheet cutting this piece (laser or plasma), followed by bending. 
3. This approach is fast and relatively cheap to obtain the desired metal piece, as one can easily see how it would look laid flat out. As for using laser or plasma cutting, it really depends on whether the laser cutter available can cut the metal sheet (thickness and material wise) and whether the rougher edges from plasma cutting are acceptable for the downstream use.
4. It is already.
5. For mass production I would likely still opt for laser cutting and bending, as laser cutting is rather fast and i suppose machines exist for automatically bending sheets of metal rather fast as well.

**Part 15**
![](Exam%20Questions%20Spring%202026/all_parts/complex_3d_printaa.jpg)
*Your answer:*
1. This is clearly a 3D printed complex part, as the nested 3D parts cannot be constructed otherwise.
2. I would use SLS for this object.
3. I would choose SLS as it is a complex part and would also need support and creating only few items that do not have to withstand any substantial pressure. SLS is picked over FDM due to support, as SLS support is the powder itself and is not "extra" things that need to be removed additionally at later points.
4. Not possible ? 
5. Unsure if there would be a case where mass production would be relevant, and do not think it is really possible with a better solution ?

**Part 24**
![](Exam%20Questions%20Spring%202026/all_parts/aaaaa.jpg)
*Your answer:*
1. A metal block with various round cuts, some of which are threaded.
2. I would use milling to manufacture this part.
3. Milling is a good choice as it gives a high quality finish. It works well with metal, especially when they are largely blocks, and therefore do not produce too much waste material from being a subtractive method.
4. It is already.
5. continue with milling & drilling.

**Part 28**
![](Exam%20Questions%20Spring%202026/all_parts/GzXjjrNMb3CQNAssuqtmTSTXmY4lk8VPzD28Vk1gpQibKjLJYVRrQKh6RrQBYW-vc7Hy5pWZr5hdkPhoHyddpPubnLKAuqFIOabn.jpg)
*Your answer:*
1. The are revolution parts with few hexagon parts.
2. I would use turning to manufacture these parts.
3. Turning is a good option as the parts are largely revolution parts, meaning they are identical revolutions around an axis. Revolution parts are produced more efficiently using turning than milling. Hex parts may be produced using milling rather than turning.
4. It is already.
5. Automatic lathe exists for mass manufacturing. 

---

## Q2 — How does it work?

*Slides: identify components → trace motor to end effector → DOFs → sensors/actuators (type + WHY) → drivers → microcontroller*

### Approach (memorize)
1. **Components:** linear guides, bearings (plain vs ball), motors, belts/gears/lead screw/rack, structure
2. **Power path:** motor → reduction (if any) → end effector
3. **Count DOFs** (usually ≈ # controlled motors)
4. **Actuators + sensors:** name type and **why** (servo = angle; stepper = steps; DC = speed/torque)
5. **Electronics layer:** driver (H-bridge, A4988, servo PWM) + microcontroller

### Practice images (`all_mechanisms/`)

**Part 01**
![](Exam%20Questions%20Spring%202026/all_mechanisms/axidraw_large_plain.jpg)
*Your answer:*
1. This is clearly a drawing machine. It has two rods as linear guides in either direction perpendicular to the drawing plane and most likely linear ball bearings on these guides. There are 2 stepper motors and 1 servo motor visible. The stepper motors drives a pulley which is connected to a belt.
2. The left-most stepper motor drives the belt that moves the platform with the second stepper motor. The second stepper motor drives the belt that moves the pen perpendicular to the direction of the first movement. The servo moves or lifts the pen from the paper to allow for switchign between drawing and pure movement sections. All three motors work together to decide the (x, y) position on the underlying 2D plane as well as whether the pen is touching the surface or not.
3. there are 3 DOFs (as described in 2)
4. Stepper motors are awesome for precise positioning, which is super relevant for the drawing machine! Servo works well for the touch / no-touch functionality as the limited 180 degree movement and known positioning along these give us the desired behavior most easily.
5. No electronics visible on the image. There must be stepper drivers and some type of micro controller to produce desired behavior. There also should be some kind of sensors for homing of the stepper motors after powering on the machine.

**Part 06**
![](Exam%20Questions%20Spring%202026/all_mechanisms/Anet-A8-High-Accuracy-3d-Printer-Prusa-i3-DIY-Kit-LCD-Screen-Printer-For-Desktop-2.jpg)
*Your answer:*
1. This is a 3D printer. It has two horisontal linear guide rods when moving the nozzle head from side to side, and one vertical linear guide rod in either side of the machine, when moving the nozzle head up and down. A lead screw is placed on either side of the machine and is driven by a stepper motor. A stepper motor on the left side uses a pulley to drive a belt which moves the mozzle head from side-to-side. We can also see a belt in the bottom underneath the printing plate, which drives the plate forwards and backwards, likely also driven by a stepper motor.
2. All motors drive either lead screws of belts directly without any further reductions. The lead screws are used in vertical movement patterns over belts as they "lock" in place and therefore are able to carry a gravitational load that belts would not. All the motors work together to move around the nozzle relative to the base plate and deposit molten plastic on the plate.
3. 3 DOFs for the nozzle head & plate, 4 if we also count a likely ingestion of plastic filament.
4. Steppers are used because of their precision. When 3D printing it is important that we align layers and movements very precisely, which is only attainable with stepping where we can ensure distances stay the same.
5. There is a screen and buttons the control the machine in the top part. Other than this, no additional electronics are visible. There must be some kinds of sensors for homing all of the stepper motors after powering on as well as stepper drivers and a microcontroller to define desired behavior.

**Part 15**
![](Exam%20Questions%20Spring%202026/all_mechanisms/Screenshot_2020-05-28%20EEZYbotARM%20MK2%20by%20daGHIZmo.png)

![](Exam%20Questions%20Spring%202026/all_mechanisms/Screenshot_2020-05-28%20EEZYbotARM%20MK2%20by%20daGHIZmo(1).png)

![](Exam%20Questions%20Spring%202026/all_mechanisms/Screenshot_2020-05-28%20EEZYbotARM%20MK2%20by%20daGHIZmo(2).png)
*Your answer:*
1. This is a robot arm that consists mainly of plastic parts and servo motors. 4 servo motors are used in total to provide movement options for the arm.
2. The servo seen on picture 1 controls the revolution movement around the base-point with a gear increasing the torque and decreasing the speed. Above this, two servos control each a base part of the arm that are connected at various joints. Lastly, a single servo controls a gripper mechanism at the end of the arm. I.e. the motors together control the 3-dimensional position of the hand as well as whether it is gripping anything.
3. 4 DOFs
4. Servos are a good choice as they are position-aware, allowing us to create neat smooth movement patterns in a limited range - similar to human arms being limited in range.
5. No additional electronics are visible on the images. Most likely an arduino or similar micro controller are used to send PWM signals to control the servos.

**Part 24**
![](Exam%20Questions%20Spring%202026/all_mechanisms/crawling_robot1.jpg)
![](Exam%20Questions%20Spring%202026/all_mechanisms/crawling_robot2.jpg)
*Your answer:*
1. The machine consists of a board with 3 rods. One rod has wheels, one is empty and one contains gears. When assembled, the empty and gear rods will be part of the M-shaped legs, while the last part of the leg will be fastened on a mount on the wheel. The robot uses a battery pack and a single DC motor.
2. The DC motor uses a worm gear construction (rotational -> rotational) to drive a gear which drives smaller gears that move the legs. The leg movements are fully restricted to the movement the the single DC motor.
3. 1 DOF
4. A DC motor is a good choice, as we need it to just keep moving forward with constant speed.
5. No additional electronics visible.

**Part 28**
![](Exam%20Questions%20Spring%202026/all_mechanisms/gripper_142078260_max.jpg)
![](Exam%20Questions%20Spring%202026/all_mechanisms/gripper_bf237650-59ec-47b8-81ce-9f20a41ddb3a.jpg)
*Your answer:*
1. This is a gripping hand consisting of four fingers with joints and a middle part which looks to be mounted on a lead screw or something similar. The middle lead screw / rod is connected to a small motor in the bottom of the machine.
2. When the motor is running, the lead screw will turn and make the middle part of the machine move downwards, effectively making the fingers close together (or the other way around of course)
3. 1 DOF
4. The main requirement i can see is that motor should be able to turn in either direction. Therefore, this DC motor would need an H-bridge driver to be able to switch direction!
5. A motor driver probably should exist in the connection to get th full functionality of the gripper.

---

## Q3 — Electronics

*Slides: read switch/pot, control DC motor, explain servo internals, wire components on breadboard. "Half of students fail the button circuit."*

### Approach (memorize)
1. **Draw schematic first** (symbols, polarity, series vs parallel)
2. **Power:** separate motor supply vs Arduino 5 V; use **transistor** for motors (Arduino can't drive high current)
3. **Every LED needs series resistor**; pot = voltage divider → `analogRead`
4. **Motors:** NPN low-side switch (1 kΩ base); H-bridge + **flyback diodes** for bidirectional DC; servo = PWM signal pin
5. **Multimeter:** voltage in **parallel**, current **in series**

### Practice images (`all_electronics/`)

**Part 04**
![](Exam%20Questions%20Spring%202026/all_electronics/DC_motor_wiring.png)
*Your answer:*

**Part 05**
![](Exam%20Questions%20Spring%202026/all_electronics/DC_stepper_motor_wiring.png)
*Your answer:*

**Part 06**
![](Exam%20Questions%20Spring%202026/all_electronics/Diagrama_The_H-Bridge_circuit_Protection-diodes-and-PWM-mode-dibujo-1024x489.png)
*Your answer:*

**Part 18**
![](Exam%20Questions%20Spring%202026/all_electronics/IMG_20200529_003750.jpg)
*Your answer:*

**Part 21**
![](Exam%20Questions%20Spring%202026/all_electronics/IMG_20200529_003846.jpg)
*Your answer:*

---

## Last-minute checklist
- [ ] Wire button + LED from memory on breadboard
- [ ] Explain your prototype: Q1 process, Q2 power path + DOFs, Q3 schematic
- [ ] Know: `V=RI`, voltage divider, injection mould design (draft, ribs, uniform walls)
