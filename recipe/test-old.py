import stim

# Verify Stim package is installed and working
try:
    assert hasattr(stim, "Circuit"), "Stim module is missing 'Circuit' class"
    print("✅ Stim package successfully imported!")
except AssertionError as e:
    print(f"❌ ERROR: {e}")
    exit(1)

# Create a quantum circuit
circuit = stim.Circuit()
circuit.append_operation("H", [0])
circuit.append_operation("CNOT", [0, 1])
circuit.append_operation("M", [0, 1]) # Ensure measurement!

print("\nCircuit:\n", circuit)

# Sample outputs
samples = circuit.compile_sampler().sample(shots=5, qubits=[0, 1])
print("\nSamples:\n", samples)
print("\nSampler Shape:\n", samples.shape)

# Validate output shape
assert samples.shape == (5, 2), f"❌ ERROR: Unexpected sample shape {samples.shape}"

# Check expected quantum behavior
# (Verifying that second qubit is always same as first due to entanglement)
expected_second_qubit = samples[:, 0]  # First column
assert (samples[:, 1] == expected_second_qubit).all(), "❌ ERROR: CNOT gate behavior mismatch"

print("\n✅ Test passed: All assertions successful!")

