# FSM – Finite State Machine

A model of computation where a system is in **exactly one state** at a time and moves to another state when a specific
event/input occurs: "If I'm in State A and event X happens → go to State B."

## Purpose

Model predictable, rule-based behavior when:

- the system has a limited number of states,
- the next action depends on the current state,
- you want something easy to reason about, test and maintain.

FSMs prevent "spaghetti" conditions by enforcing explicit transitions and make behavior deterministic. Typical uses:
authentication/checkout/onboarding flows, devices (a door: Open → Closing → Closed), UI navigation, protocols and
parsers.

## Components

1. **States** – distinct modes (Idle, Loading, Error…).
2. **Initial state** – where it starts.
3. **Events / inputs** – external triggers (button press, message, signal).
4. **Transitions** – rules for moving between states.
5. Optional **actions** – side effects on entering/exiting a state or during a transition.

## How it works

1. Machine starts in the initial state.
2. An event occurs.
3. Is there a valid transition for (current state, event)?
4. Yes → move to the next state, run actions. No → ignore the event or raise an error.
5. Repeat.

## Example – order lifecycle

| State     | Event     | Next state  |
|-----------|-----------|-------------|
| `created` | `pay`     | `paid`      |
| `created` | `cancel`  | `cancelled` |
| `paid`    | `ship`    | `shipped`   |
| `paid`    | `refund`  | `cancelled` |
| `shipped` | `deliver` | `delivered` |

Anything not in the table (e.g. `shipped` + `cancel`) is invalid.
