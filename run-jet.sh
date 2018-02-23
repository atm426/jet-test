#!/bin/bash

rm /Users/austin/research/jet-test/checkpoints/checkpoint_*.h5
cd /Users/austin/research/Jet
mpirun -n 8 ./jet
mv checkpoint_*.h5 /Users/austin/research/jet-test/checkpoints/