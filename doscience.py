from multiprocessing import Pool

## exploration and discovery
try:
    from PriorExperience import insight, serendipity
    my_new_idea = gen_ideas(insight, serendipity, NewTechnology)
except:
    my_new_idea = copy.copy(somebody_elses_idea)

## get funding and build a team
funded = False
while not funded:
    proposal = gen_proposal(my_new_idea).submit()
    wait(SIX_MONTHS)
    funded = proposal.was_funded

grads = Pool(5)
postdocs = Pool(3)
undergrads = Pool(8)

## do the work and write it up
results = get_data(grads, postdocs, undergrads, proposal.cash).findresult()
paper = results.write_paper()
paper.submit(journal="Science")  # this will be accepted without revision

## reap rewards
cv_item = collect_prize(type="Nobel", thank=",".join([x.name for x in grads]))
