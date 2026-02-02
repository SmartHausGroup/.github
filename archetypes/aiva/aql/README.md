# AQL — AIVA Query Language

**Chemistry layer of AIVA: symbolic query language and provable execution graphs**

Part of the **AIVA** archetype. [← Back to AIVA](../README.md)

## Role

AQL (AIVA Query Language) is the **Chemistry layer** of the triadic AIVA system. It consumes the plans and blueprints produced by AIOS (Biology) and compiles them into **mathematically provable execution graphs**—DAGs—expressed as molecules, atoms, chemical bonds, and equilibrium (proofs). AQL does not execute; it **structures**. It type-checks intent, resolves symbolic contracts, applies structural calculus (IDSC, MDO), and verifies acyclicity and invariants so that what reaches AEF (Physics) is a first-class, auditable blueprint. The chemistry layer exists because **structure** is where we prove correctness: intent is fluid (natural language, policy, memory); execution is parallel and stateful at runtime; the intermediate representation in AQL is **static and deterministic**. We prove the DAG is correct *before* any particle runs, optimize at compile time (DAG tuning, resource allocation), and treat the blueprint as an artifact we can replay, audit, and enforce (A4). Without AQL we would compile intent directly to execution and lose the ability to **prove** what we are about to run.

## Key features

AQL provides **static deterministic graphs** (DAGs) so that mathematical correctness and provability are decoupled from execution. **Symbolic contract resolution** gives a formal specification of computational intent; the **mathematical proof system** supports formal verification of correctness. **Type safety** guarantees contract resolution properties, and **compile-time optimization** handles DAG performance and resource allocation so that the execution layer receives a validated, optimized plan rather than ad-hoc instructions.

## Mathematical foundation

AQL is governed by the **Contract Resolution Operator** (formal calculus for intent resolution), **Intent-Driven Structural Calculus (IDSC)** (parallelism and structure), **Mutation Differential Operator (MDO)** (telemetry-driven adaptation), and **Entropy Axioms** (mathematical constraints and validation). These operators and axioms are defined in the lattice cognitive calculus and enforced so that every AQL output conforms to the runtime symbol map and runtime function contracts.

## Integration

**AIOS** produces parsed intent and blueprints that AQL compiles into DAGs. The SNS hands off molecule-level plans; AQL turns them into typed, acyclic graphs with resolved contracts and verified invariants. No execution occurs in AQL; the output is a blueprint.

**AEF** receives from AQL the compiled DAGs and turns them into particle instructions for execution. AQL’s output is the only input AEF needs to schedule and run particles; the chemistry layer guarantees that the structure is correct before execution begins.

**RFS** can store symbolic structures and contracts produced or consumed by AQL, so that blueprints and contract definitions are persistent and auditable alongside the rest of the system’s state.
