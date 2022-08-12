"""Cheeky Julia example to compare to the base Python version."""

function fib(limit::Int)::Array{Int}
    numbers::Array{Int} = [0, 1, 1]

    current::Int = 1
    while current < limit
        current = numbers[end-1] + numbers[end]
        push!(numbers, current)
    end
    return numbers
end

fib(0) # jit-compile

initial_time = time()
for _ in 1:1_000_000
    fib(1_000_000)
end

println("Result is: ", fib(1_000_000))
println("Time taken: ", time() - initial_time)
