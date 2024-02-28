function map = TrainMapAdaptive(mset0, objective, atm_options)
    mexOptions = atm_options.getMexOptions;
    mset_ids = arrayfun(@(mset) mset.get_id(), mset0);
    input_str=['map_ptr = MParT_(',char(39),'ConditionalMap_TrainMapAdaptive',char(39),',mset_ids,objective.get_id()'];
    for o=1:length(mexOptions)
        input_o=[',mexOptions{',num2str(o),'}'];
        input_str=[input_str,input_o];
    end
    input_str=[input_str,');'];
    eval(input_str);
    map = ConditionalMap(map_ptr,"id");
end