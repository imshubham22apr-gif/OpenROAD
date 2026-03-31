# Chipathon Workflow and Challenges

Chipathon is an open-source hardware event that encourages developers to create their own custom chip designs using automated tools. It's an intense, community-driven "hackathon-style" event where individuals or teams go from concept to a complete RTL-to-GDSII flow within a few weeks or months. This document outlines the typical workflow and common challenges faced by Chipathon participants.

## What is Chipathon?

Chipathon is more than just a competition; it is a movement to democratize the entire chip design stack. By combining educational resources with powerful open-source tools like OpenROAD and the SKY130/GlobalFoundries process development kits (PDKs), Chipathon empowers anyone with a basic knowledge of digital logic to create their own custom IC.

## Typical Chipathon Workflow

The Chipathon workflow is designed to be streamlined and highly iterative. It generally follows these stages:

1. **Ideation and Specification**: Teams brainstorm a project idea, define its features, and create a high-level block diagram. Projects often include IoT modules, specialized cryptography engines, or AI accelerators.
2. **RTL Design and Simulation**: The core of the chip's logic is written in Verilog or Chisel and then tested in simulation (using tools like Icarus Verilog or Verilator) to ensure it works according to the design specification.
3. **Physical Implementation**: This is where OpenROAD enters the picture. The synthesized RTL is passed through the automated physical design flow, which includes floorplanning, placement, and routing.
4. **Verification and Signoff**: Participants must verify that their final layout is both functionally correct and manufacturable. This involves running DRC, LVS, and timing checks to confirm the design meets all foundry requirements.
5. **Tapeout Submission**: Once the design is ready, it is submitted for manufacturing through a multi-project wafer (MPW) shuttle program.

## Common Challenges

Designing a chip is not without its hurdles. Chipathon participants often encounter several key challenges:

- **Timing Violations**: Ensuring that signals travel through the gates and wires within the required clock cycle can be difficult as designs become more complex.
- **Congestion**: When there are too many gates in a small area, routing wires between them becomes impossible, leading to a failure to route.
- **Tools and Environment**: Using cutting-edge open-source tools sometimes means dealing with bugs or incomplete documentation, which requires patience and a "maker" spirit.

Despite these challenges, Chipathon offers an unparalleled learning experience. It bridges the gap between software and hardware engineering, allowing participants to see their code literally turned into silicon.
