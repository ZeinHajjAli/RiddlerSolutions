% Zein Hajj-Ali

global rates
rates = zeros(1000,1000);

for f = 1:1000
    for a = 1:1000
        fprintf("When fallen are %f and alive are %f, the winRate = %f \n", f, a, battleSim(f, a));
    end
end



function [winRate] = battleSim(fallen, alive)
% sim: Recursive function to calculate the win probability in a battle between
% the fallen and the alive when the individual probability is 0.5. When the
% fallen win, they add 1 to their number while subtracting one from the alive.
% When the alive win, they subtract one from the fallen's number without adding
% to their own.
%
% INPUTS:
%   fallen: Number of soldiers in the fallen army
%   alive: Number of soldiers in the alive army
%
% OUTPUTS:
%   winRate: double value that represents the probaility of the alive winning

global rates

if fallen < 1
    winRate = 1.0;
else
    if alive < 1
        winRate = 0.0;
    else
        if fallen < length(rates(:,alive)) && alive < length(rates(fallen,:)) && rates(fallen, alive) > 0
            winRate = rates(fallen, alive);
        else
            fallenProb = 0.5*battleSim(fallen+1, alive-1);
            aliveProb = 0.5*battleSim(fallen-1, alive);
            rates(fallen, alive) = fallenProb + aliveProb;
            winRate = rates(fallen, alive);
        end
    end
end

end
