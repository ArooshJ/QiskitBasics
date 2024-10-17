print ("Hello Quantum World")

# Notes 
# to start: -- 
# import numpy as np
# from qiskit import QuantumCircuit


# Pauli Gates:

# Pauli-X gate (NOT gate): 
# Syntax: qc.x(qubit)

# Pauli-Y gate: Syntax:
#  qc.y(qubit)

# Pauli-Z gate: Syntax: 
# qc.z(qubit)

# Hadamard Gate: Syntax:
#  qc.h(qubit)


# Phase Gate = pmgate: Syntax: 
# qc.p(theta, qubit), where theta is the phase angle in radians.

# S gate or root(t) gate
# qc = QuantumCircuit(q)
# qc.s(q)
# qc.sdg(q)
# qc.draw()

# T = root(s) and T† (T-dagger) Gates: 
# Syntax: qc.t(qubit) (T gate) Syntax: 
# qc.tdg(qubit) (T-dagger gate)

# Rotation Gates: 
# Syntax: qc.rx(theta, qubit), where theta is the rotation angle around the x-axis in radians. Syntax: qc.ry(theta, qubit), where theta is the rotation angle around the y-axis in radians. Syntax: qc.rz(theta, qubit), where theta is the rotation angle around the z-axis in radians.

# Controlled Gates:
#  Syntax: qc.cx(control_qubit, target_qubit) (CNOT gate) Syntax: qc.ccx(control_qubit1, control_qubit2, target_qubit) (Toffoli gate)

# Swap Gate: 
# Syntax: qc.swap(qubit1, qubit2)

# Barrier Gate:
#  Syntax: qc.barrier(qubits), where qubits is an optional list of qubits to apply the barrier.

# Measurement: 
# Syntax: qc.measure(qubit, classical_bit), where qubit is the qubit to measure, and classical_bit is the classical bit to store the measurement result.

# Reset: Syntax:
#  qc.reset(qubit), to reset a qubit to the |0⟩ state.

# Identity Gate:
# Syntax: qc.i(qubit), for the identity gate (no operation).

# U3 Gate: Syntax: 
# qc.u3(theta, phi, lambda, qubit), where theta, phi, and lambda are rotation angles in radians.

# U2 Gate: Syntax: 
# qc.u2(phi, lambda, qubit), where phi and lambda are rotation angles in radians.

# U1 Gate: Syntax:
#  qc.u1(lambda, qubit), where lambda is the phase angle in radians.

# PauliRot Gate: Syntax:
# qc.pauli(pauli_string, qubits), where pauli_string is a Pauli operator string and qubits is the list of qubits to apply the Pauli rotation.

# PauliSum Gate: Syntax: 
# qc.pauli_sum(pauli_sum, qubits), where pauli_sum is a sum of Pauli operators and qubits is the list of qubits to apply the PauliSum gate.

# Note: The syntax examples assume that you have already created a QuantumCircuit object named q

 
  
# qc = QuantumCircuit(q)
# qc.rx(theta,q)
# qc.draw()

# qc = QuantumCircuit(q)
# qc.ry(theta,q)
# qc.draw()

# qc = QuantumCircuit(q)
# qc.rz(theta,q)
# qc.draw()

# As shown in the examples below, this operation is implemented in Qiskit as cU(q[0],q[1]).
# If qubit 1 is the control and qubit 0 is the target, then the basis vectors are transformed according to

# qc = QuantumCircuit(q)
# qc.cx(q[0],q[1])
# qc.draw()

# qc = QuantumCircuit(q)
# qc.cy(q[0],q[1])
# qc.draw()

# qc = QuantumCircuit(q)
# qc.cz(q[0],q[1])
# qc.draw()

# qc = QuantumCircuit(q)
# qc.ch(q[0],q[1])
# qc.draw()

# qc = QuantumCircuit(q)
# qc.cp(pi/2,q[0],q[1])
# qc.draw()

# qc = QuantumCircuit(q)
# qc.crz(pi/2,q[0],q[1])
# qc.draw()

# qc = QuantumCircuit(q)
# qc.cu(pi/2, pi/2, pi/2, 0, q[0], q[1])
# qc.draw()

# tofolli = ccx gate
# qc = QuantumCircuit(q)
# qc.ccx(q[0], q[1], q[2])
# qc.draw()

# qc = QuantumCircuit(q)
# qc.cswap(q[0], q[1], q[2])
# qc.draw()

# qc = QuantumCircuit(q, c)
# qc.x(q[0]).c_if(c, 0) ## if dtatement
# qc.measure(q,c)
# qc.draw()

# Here the classical bit always takes the value 0 so the qubit state is always flipped.
#        ┌───┐ ┌─┐
#  q27: ─┤ X ├─┤M├
#        └─╥─┘ └╥┘
#       ┌──╨──┐ ║
# c0: 1/╡ 0x0 ╞═╩═
#       └─────┘ 0 