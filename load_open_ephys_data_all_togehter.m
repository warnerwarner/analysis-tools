function res = load_open_ephys_data_all_togehter(folderpath)
con_files = dir(char(strcat(folderpath, '\100_CH*.continuous')));
res = struct();
for i =1:length(con_files)
    chan_name = con_files(i).name;
    if contains(chan_name, 'CH')
        disp(chan_name)
        res(i).name = chan_name;
        res(i).data = load_open_ephys_data_faster(strcat(folderpath,'\', chan_name));
    end
end