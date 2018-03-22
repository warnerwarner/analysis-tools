function res = load_open_ephys_data_all_togehter(folderpath)
con_files = dir(char(strcat(folderpath, '\*.continuous')));
res = struct();
for i =1:length(con_files)
    chan_name = con_files(i).name;
    disp(chan_name)
    res.con_files(i).name = load_open_ephys_data_faster(strcat(folderpath,'\', chan_name));
end