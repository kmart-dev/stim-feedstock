import stim

print("✅ stim imported")

# Build a basic circuit
c = stim.Circuit()
c.append_operation("H", [0])
c.append_operation("M", [0])

print("✅ circuit created and measured")

# Try sampling
sampler = c.compile_sampler()
samples = sampler.sample(3)

print("✅ samples:")
print(samples)

