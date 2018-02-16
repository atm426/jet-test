#!/bin/bash

cd /Users/austin/research/Jet
mpirun -n 4 ./jet
mv checkpoint_*.h5 /Users/austin/research/jet-test/checkpoints/