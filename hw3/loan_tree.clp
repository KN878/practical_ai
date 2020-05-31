(defrule broke-ass-criminal
    (earns ?broke ?income)
    (test (< ?income 30))
    (is ?broke criminal)
    => 
    (printout t ?broke " has received loan as he/she is a broke-ass criminal" crlf)
    (assert(has ?broke loan))
)

(defrule broke-ass-honest-citizen
    (earns ?broke ?income)
    (test (< ?income 30))
    (is ?broke honest citizen)
    =>
    (printout t ?broke " has not received loan as he/she is a broke-ass honest citizen" crlf)
    (assert(has no ?broke loan))
)

(defrule avg-citizen
    (earns ?citizen ?income)
    (job years ?citizen ?years)
    (test (<= ?income 70))
    (test (>= ?income 30))
    =>
    (assert (medium-income-citizen ?citizen ?years))
)

(defrule years-less-one
    (medium-income-citizen ?citizen ?years)
    (test (< ?years 1))
    =>
    (printout t ?citizen " has not received loan due to low job years experience" crlf)
    (assert(has no ?citizen loan))
)

(defrule years-one-to-five
    (medium-income-citizen ?citizen ?years)
    (test (>= ?years 1))
    (test (<= ?years 5))
    =>
    (assert(credit payments check ?citizen))
)

(defrule has-credit-payments
    ?check <- (credit payments check ?citizen)
    (credit payments exists ?citizen)
    =>
    (printout t ?citizen " has received loan" crlf)
    (retract ?check)
    (assert(has ?citizen loan))
)

(defrule no-credit-payments
    ?check <- (credit payments check ?citizen)
    (no credit payments exists ?citizen)
    =>
    (printout t ?citizen " has not received loan due to poor credit history" crlf)
    (retract ?check)
    (assert(has no ?citizen loan))
)

(defrule years-more-five
    (medium-income-citizen ?citizen ?years)
    (test (> ?years 5))
    =>
    (printout t ?citizen " has received loan" crlf)
    (assert(has ?citizen loan))
)

(defrule rich-ass-batya
    (earns ?batya ?income)
    (test (> ?income 70))
    (is ?batya honest citizen)
    =>
    (printout t ?batya " has received loan" crlf)
    (assert(has ?batya loan))
)



(defrule rich-ass-criminal
    (earns ?trapper ?income)
    (test (> ?income 70))
    (is ?trapper criminal)
    =>
    (printout t ?trapper " has not received loan" crlf)
    (assert(has no ?trapper loan))
)

(reset)

(assert
    (earns markel 29)
    (is markel criminal)
    
    (earns michel 28)
    (is michel honest citizen)
    
    (earns avg1 35)
    (job years avg1 0.9)
    
    (earns avg2 35)
    (job years avg2 1.5)
    (credit payments exists avg2)
    
    (earns avg3 35)
    (job years avg3 1.5)
    (no credit payments exists avg3)
    
    (earns avg4 35)
    (job years avg4 6)

    (earns timur 71)
    (is timur criminal)
    
    (earns nikita-top 105)
    (is nikita-top honest citizen)
    
)

(run)
(facts)
