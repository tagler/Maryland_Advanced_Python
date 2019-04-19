from mpi4py import MPI

comm = MPI.COMM_WORLD
workers = comm.Get_size()

def square(n):
    return n*n

data = list(range(-10,10))

chunk = comm.scatter([data[n::workers] for n in range(workers)], root=0)
chunk = [square(n) for n in chunk]
parallel = comm.gather(chunk)

if comm.Get_rank() == 0:
    print(list(parallel))


