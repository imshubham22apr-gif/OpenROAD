# RTL to GDSII Flow

The RTL to GDSII flow is the sequence of steps that transforms a Register Transfer Level (RTL) description (usually written in Verilog or VHDL) into a final Graphic Data System (GDSII) layout that can be manufactured by a foundry. In an automated toolset like OpenROAD, this flow is divided into several clear, interdependent stages. Understanding each stage is crucial for any hardware designer.

## Synthesis

Synthesis is the first major step. It takes the high-level RTL code and maps it to a specific library of primitive digital gates provided by a semiconductor foundry. For example, a simple `if` statement or a state machine is converted into a netlist containing NAND gates, flip-flops, and other standard cells. The goal of synthesis is to meet the design's functional requirements while optimizing for area, power, and timing.

## Floorplanning

Floorplanning is the first physical design step. It defines the size and shape of the chip and determines the placement of I/O pins, power rings, and large components like memory blocks (SRAMs). A good floorplan minimizes congestion and ensures that power can be distributed evenly across the entire chip.

## Placement

Placement is the process of positioning all the small standard cells from the synthesized netlist onto the chip's rows within the floorplanned area. This is often done in two phases:
1. **Global Placement**: Cells are roughly distributed across the chip to avoid overlap and minimize wire length.
2. **Detailed Placement**: Each cell is moved onto a legal row and grid location while respecting design rules.

## Clock Tree Synthesis (CTS)

Once the cells are placed, the clock signal must be delivered to every flip-flop with minimal skew and delay. CTS builds a tree-like network of buffers to distribute the clock reliably. A poorly designed clock tree can lead to timing violations and high power consumption.

## Routing

Routing is the process of physically connecting the pins of the placed cells using metal layers. It is also done in two phases:
1. **Global Routing**: Determines the general paths for the nets through various regions of the chip.
2. **Detailed Routing**: Lays down the actual metal wires while following all the complex design rules of the foundry.

## Signoff and GDSII Export

The final step is signoff, where the design is checked against the foundry's rules through tools like Design Rule Check (DRC) and Layout Versus Schematic (LVS). After the design is verified, it is exported as a GDSII file—the industrial standard for physical layout data—and sent to the foundry for fabrication.
