from first import cleanup, something_else, main
from second import run_em


run_em()
main()
cleanup()
something_else()

print(f'Third Modules Name: {__name__}')
