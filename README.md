# Kaon Decay Experiment

Two Python classes that simulate a beam of Kaons decaying into plus Pions and minus Pions and collects the resultant data and graphs them using histograms. The makedecay class produces a Kaon decay, making sure it has the correct energy and decay location. By using the class function getdecay(), from the makedecay class, we get the location of the decay and the four-momentum of the resultant plus Pion and minus Pion. 
The Kaon_Decay class uses the four-momentum and decay location to calculate future locations of the two Pions. Using the future locations, we can check if the Pions collide with either of the three detectors. 
Different values of the experiment are graphed using a histogram class that my professor created. One of the values graphed includes the energy of the Pions that hit the detector.

## Getting Started

Once the files are downloaded you can load the Kaon_decay class into a Python IDE and run the code. You can also run the code by typing the following command into Bash.
```bash
python Kaon_Decay.py
```
After running the code there will be seven histograms generated with the resultant data.

### Installing

Download the Python files in the same destination.

