% Creates a trial specific spectrogram, currently takes a single trial

function [s,f,t] = average_spectrogram(data, trial_times, Fs)

% The spectrogram takes the trace over the trial and samples from one to
% one hundred hertz. The window values need to be large enough that they
% can accurately find the relatively low frequency range, so for a Fs of
% 30000 a window of 3000 is chosen as it can transform to frequencies of
% >~10Hz, which when the range of comparrison will be from 30-50 is a good
% value. The overlap can be edited depending on how 'smooth' the plot
% should look

names = fieldnames(trial_times);



    
for i = 1:length(names)
    disp(i)
    for j =1:length(trial_times.(names{i}))
        start = trial_times.(names{i})(j, 1);
        stop = trial_times.(names{i})(j, 2);
        spectrogram(data(start:stop), 3000, [], 1:0.1:100, Fs, 'yaxis', 'MinThreshold', 0)
    end
end

