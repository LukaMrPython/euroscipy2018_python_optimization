def OU_process2(num_steps, *, δt=0.1, x0=0, τ=1, σ=2):
    N_norm = memoryview(np.random.randn(num_steps))
    
    relax = math.exp(-δt / τ)
    diffuse = σ * math.sqrt(1 - relax**2)

    x = [x0]
    for i in range(num_steps):
        x.append(
            x[-1] * relax + diffuse * N_norm[i]
        ) 
    return x