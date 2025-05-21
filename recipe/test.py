import stim

circuit = stim.Circuit()
circuit.append_operation("H", [0])
circuit.append_operation("CNOT", [0, 1])
print("Circuit:")
print(circuit)

samples = circuit.compile_sampler().sample(shots=5)
print("Samples:")
print(samples)
