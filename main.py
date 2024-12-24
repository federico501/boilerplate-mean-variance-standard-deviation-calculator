# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std as st
from unittest import main

result=st.calculate([2,6,2,8,4,0,1,5,7])

print(result)

# Run unit tests automatically
main(module='test_module', exit=False)