mkdir wav
for /l %%f in (1,1,800) do copy daisy.wav %~dp0wav\%%f.wav