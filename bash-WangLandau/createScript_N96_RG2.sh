#!bin/bash

nameFolder="N96_SA_E0.4_Rg2"

newFileBase="WL_N96_SA_E0.4_Rg"

newBFMFileBase="LinearChain_N96_PerXYZ256_NNShell_E0.4_f1.01"

mkdir $nameFolder

#array=(1.0 $(seq -20.0 -50.0 -240.0) -350.0)

#array=(700.0 $(seq 600.0 -20.0 10.0) -1.0)
#array=(-1.0 $(seq 100.0 150.0 1800.0) 2100.0)
array=(1.0 $(seq -60.0 -60.0 -1800.0) -2100.0)
#array=( 1.0 -20.0 -40.0 -60.0 -80.0 -100.0 -120.0 -140.0 -160.0 -180.0 -200.0 -220.0 -240.0 -350.0)
#overlap=20.0
overlap=20.0

#minhisto=-1.05
#maxhisto=30001.05
maxhisto=1.05
minhisto=-30001.05
bins=300021

save=1000
minstatistic=10000
hglndosfile="LinearChain_N96_PerXYZ256_NNShell_E0.4_f1.01_HGLnDOS_shifted"


# get length of an array
arraylength=${#array[@]}

# use for loop to read all values and indexes
for (( i=0; i<${arraylength}-1; i++ ));
do
  echo $i " / " ${arraylength} " : " ${array[$i]}
  minwin=${array[$i+1]}
  #maxwin=$(echo "scale=8; ${array[$i]}+${overlap}" | bc)
  maxwin=${array[$i]}
  
  # if the array is in ascending order
  if (( $(echo "$minwin > $maxwin" | bc -l) ));
  then
    minwin=${array[$i]}
    maxwin=$(echo "scale=8; ${array[$i+1]}+${overlap}" | bc)
    
  else
    # decending order
    minwin=${array[$i+1]}
    maxwin=$(echo "scale=8; ${array[$i]}+${overlap}" | bc)
  fi
  
  echo $i " min/max = (" ${minwin} " : " ${maxwin} ")"
  
  postfix=$(echo $(echo "scale=8; ${i}+1" | bc) | awk '{printf "%03d\n", $1}')"v"$(echo $(echo "scale=8; ${arraylength}-1" | bc) | awk '{printf "%03d\n", $1}')
  
  newFileBaseSlurm=$newFileBase$postfix
  
  cp "input_RG2.slurm" $nameFolder"/"$newFileBaseSlurm".slurm"
  cp $hglndosfile".dat" $nameFolder
  newFile=$newBFMFileBase"_"$postfix
  cp $newBFMFileBase".bfm" $nameFolder"/"$newFile".bfm"
  
  sed -i 's/input/'$newFileBaseSlurm'/g' $nameFolder"/"$newFileBaseSlurm".slurm"
  sed -i 's/BFMFILE/'$newFile'/g' $nameFolder"/"$newFileBaseSlurm".slurm"
  sed -i 's/MINWIN/'$minwin'/g' $nameFolder"/"$newFileBaseSlurm".slurm"
  sed -i 's/MAXWIN/'$maxwin'/g' $nameFolder"/"$newFileBaseSlurm".slurm"
  sed -i 's/MINHISTO/'$minhisto'/g' $nameFolder"/"$newFileBaseSlurm".slurm"
  sed -i 's/MAXHISTO/'$maxhisto'/g' $nameFolder"/"$newFileBaseSlurm".slurm"
  sed -i 's/BINS/'$bins'/g' $nameFolder"/"$newFileBaseSlurm".slurm"
  sed -i 's/SAVEMCS/'$save'/g' $nameFolder"/"$newFileBaseSlurm".slurm"
  sed -i 's/MINSTATISTIC/'$minstatistic'/g' $nameFolder"/"$newFileBaseSlurm".slurm"
  sed -i 's/HGLNDOSFILE/'$hglndosfile'/g' $nameFolder"/"$newFileBaseSlurm".slurm"
  
  
done

# extract and merge if neccessary
# for i in *.slurm; do echo $(sed -n '29,29p;30q' $i) >> runN256.sh; done


