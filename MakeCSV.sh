!/bin/bash


# Basic Script to create campus csv files for new equipent

#################################################################

cat jhart_shell_logo.txt
echo -e "\n"
echo "#################################################################################"
echo "#################################################################################"
echo -e "\n"
#################################################################

	echo "Please enter the cart name."
	read _Cart
	echo "Please enter the PO Number for this order."
	read _Po
	echo "Please enter how many units will be in this cart."
	read _Units
	echo "Please enter the Inventory Year.(YY)"
	read _Year
	echo "Please enter the semester code. (FA, SP, SU)"
	read _SemCode
	echo "Please enter the type of unit (example: 'P' is printer, 'CB' is chromebook."
	read _UnitType
	echo "Please enter the starting unit number."
	read _StartNum
	echo "You entered "$_StartNum""
	echo "Please enter the ending unit number."
	read _EndNum
	echo "You entered "$_EndNum" as the last unit number."
	_NewFile="$_Cart-PO$_Po-Units$_Units-$_StartNum-$_EndNum"
	echo "Your new CSV file will be named "$_NewFile", Is this correct? y/n"
	read _Yn
	case $_Yn in
		[Yy]* )
			_RepeatCheck=$(cat *.csv | grep "$_StartNum")
			if [ "" == "$_RepeatCheck" ];
			then
				cp CSVTemplate $_NewFile.csv
				for (( i=$_StartNum; i<=$_EndNum; i++))
					do
						echo $_Year$_SemCode$i$_UnitType,,, >> $_NewFile.csv
				done
				cat $_NewFile.csv
				wc -l $_NewFile.csv
			else
			echo "Error, you have entered a duplicate Unit Number"
			exit
			fi
			;;
		[Nn]* ) echo "Going to cancel creation of CSV file, please rerun the script once you are returned to your terminal."
			sleep 4
			;;
		* ) echo "Please answer with (y) for yes or (n) for no."
	esac
exit



