#!/bin/bash
#SBATCH --job-name=download           # Job name
#SBATCH --mail-type=END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=ignasi.valles@gmail.com     # Where to send mail    
#SBATCH --ntasks=1                    # Run on a single CPU
#SBATCH --output=serial_test_%j.log   # Standard output and error log

# Define your CMEMS Login credentials
conda activate py3_parcels2v4

CMEMS_USERNAME="ivalles"
CMEMS_PWD="3cants3roses"

# Define both starting and ending date
# Apply standard format to avoid errors - Use backticks ` and not apostroph '
#current_date=`date +"%Y-%m-%d" -d "$STARTING_DATE"`" 12:00:00"
#loop_end_date=`date +"%Y-%m-%d" -d "$ENDING_DATE"` " 12:00:00"
#echo $current_date, 'CD1'


#current_date="2010-01-01 12:00:00"


OUTPUT_DIR="/mnt/lustre/users/valles/DATA/CMEMS_forecast_PHY_surf/"
FILENAME="eA_hourly"
IFS=''
startdate=20211101
enddate=20220530

d=
n=0

until [ "$d" = "$enddate" ]
do

((n++))
d=$(date -d "$startdate + $n days" +%Y-%m-%d)
ti=''$d' 00:30:00'
tf=''$d' 23:30:00'
tname=''$d'.nc'
echo $ti

python -m motuclient --motu https://nrt.cmems-du.eu/motu-web/Motu --service-id GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS --product-id cmems_mod_glo_phy_anfc_merged-uv_PT1H-i --longitude-min -50 --longitude-max 15 --latitude-min -15 --latitude-max 15 --date-min $ti --date-max $tf --depth-min 0.494 --depth-max 0.4941 --variable uo --variable utide --variable utotal --variable vo --variable vsdx --variable vsdy --variable vtide --variable vtotal --out-dir $OUTPUT_DIR --out-name $tname --user ivalles --pwd 3cants3roses

done