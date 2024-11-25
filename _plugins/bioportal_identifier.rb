module CustomFilter
  def make_bioportal_id(obo_id)
    return obo_id unless obo_id.is_a?(String)

    # ID requirements should be locked down moving forward, so additions to this table
    # should be rare
    special_cases = {
      'fbbt' => 'FB-BT',
      'ro' => 'OBOREL',
      'apollo_sv' => 'APOLLO-SV',
      'trans' => 'PTRANS',
      'wbls' => 'WB-LS',
      'fbdv' => 'FB-DV',
      'wbbt' => 'WB-BT',
      'wbphenotype' => 'WB-PHENOTYPE',
      'to' => 'PTO',
      'fbcv' => 'FB-CV',
      'mod' => 'PSIMOD',
      'pso' => 'PLANTSO'
    }

    return special_cases[obo_id] if special_cases.key? obo_id

    obo_id == obo_id.downcase ? obo_id.upcase : obo_id
  end
end

Liquid::Template.register_filter(CustomFilter)
