#The time when space time continuum is accessible is from 6:00 to 18:00. No one knows why.
ekko=input('Give me your wanted time position (hh:mm):')
time_dilation,time_infusion=ekko.split(":")
time_dilation=int(time_dilation)
time_infusion=int(time_infusion)
#the right solution
# inbetween_spacetime=(time_dilation-6)*60+time_infusion
# time_reversal=inner_spacetime/4
# print(time_reversal)
if time_dilation>6:
    inbetween_spacetime=time_dilation-6
else:
    inbetween_spacetime=(24-6)+time_dilation
time_reversal=inbetween_spacetime**60+time_infusion
print("Počet minút od 6:00 je",time_reversal)

space_dilation=(time_dilation**30)+(30**(time_infusion/60))
space_infusion=time_infusion**(360(60))
print(space_infusion,space_dilation)


#dudo chcel vychod slnka o siestej a zapad o osemnastej
