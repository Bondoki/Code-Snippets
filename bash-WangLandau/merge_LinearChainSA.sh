#!bin/bash


newBFMFileBase="LinearChain_N64_PerXYZ128_NNShell_SA_E"

newOutputDat="RG2.dat"

array=(-0.01 $(seq -0.02 -0.02 -0.80) -1.00)

# get length of an array
arraylength=${#array[@]}

# use for loop to read all values and indexes
for (( i=0; i<${arraylength}; i++ ));
do
  echo $i " / " ${arraylength} " : " ${array[$i]}
  
  
  postfix=$(echo $(echo "scale=8; ${array[$i]}" | bc) | awk '{printf "%1.2f\n", $1}')"_"$(echo $(echo "scale=8; ${i}+1" | bc) | awk '{printf "%03d\n", $1}')"v"$(echo $(echo "scale=8; ${arraylength}-1" | bc) | awk '{printf "%03d\n", $1}')
  
  
  newFile=$newBFMFileBase$postfix"_Rg2.dat"
  echo $newFile
  
  # specify here the lines in your Rg2.dat file to extract
  entry=${array[$i]}" "$(sed -n '23,23p;24q' $newFile)
  echo $entry
  
  echo $entry >> $newBFMFileBase"_"$newOutputDat
  
done

