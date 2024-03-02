#include "subset.h"

#include "../../generator_data.h"


namespace dlplan::generator::rules {
void SubsetConcept::generate_impl(const core::States& states, int target_complexity, GeneratorData& data, core::DenotationsCaches& caches) {
    if (target_complexity == 3) {
        core::SyntacticElementFactory& factory = data.m_factory;
        for (int i = 1; i < target_complexity - 1; ++i) {
            int j = target_complexity - i - 1;
            for (const auto& r1 : data.m_roles_by_iteration[i]) {
                for (const auto& r2 : data.m_roles_by_iteration[j]) {
                    auto element = factory.make_subset_concept(r1, r2);
                    auto denotations = element->evaluate(states, caches);
                    if (data.m_concept_hash_table.insert(denotations).second) {
                        data.m_reprs.push_back(element->str());
                        data.m_concepts_by_iteration[target_complexity].push_back(std::move(element));
                        increment_generated();
                    }
                }
            }
        }
    }
}

std::string SubsetConcept::get_name() const {
    return "c_subset";
}
}
