set style data dots
set nokey
set xrange [0: 3.83552]
set yrange [ -6.11172 : 18.82644]
set arrow from  0.96280,  -6.11172 to  0.96280,  18.82644 nohead
set arrow from  1.64361,  -6.11172 to  1.64361,  18.82644 nohead
set arrow from  2.03667,  -6.11172 to  2.03667,  18.82644 nohead
set arrow from  2.59255,  -6.11172 to  2.59255,  18.82644 nohead
set xtics ("G"  0.00000,"L"  0.96280,"K"  1.64361,"X"  2.03667,"W"  2.59255,"G"  3.83552)
 plot "GaAs_band.dat"
