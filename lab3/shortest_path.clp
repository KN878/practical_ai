(defrule reverse
    (path ?x ?y)
    =>
    (assert(path ?y ?x))
;;;
;;; add here reverse edge
;;;
)

; create trivial chains out of edges
(defrule chain
    (path ?x ?y)
    =>
; (chain from to distance where-to-go-first)
    (assert(chain ?x ?y 1 ?y))
)

; create longer chains
(defrule glue_chain
    (chain ?x ?y ?d1 ?via1)
    (chain ?y ?z ?d2 ?via2)
    (not (chain ?x ?z ?d3 ?via3))
    (test (< (+ ?d1 ?d2) 6))
    (test (<> (str-compare ?x ?z) 0))
    =>
    (assert(chain ?x ?z (+ ?d1 ?d2) ?via1))
;;;
;;; TODO: create longer chain as concatenation of 2 short 
;;;
)
                     
; trigger path search. add new fact type "bt" - backtrace request.
; similar to query, but does not trigger new search and holds distance
(defrule findpath
    (chain ?x ?y ?d ?via)
    (query ?x ?y)
    (test (< ?d 6))
    =>
    (printout t ?x " to " ?y " via " ?via ", distance " ?d crlf)
    (assert(bt ?via ?y (- ?d 1)))
)

; backtrace shorter path until we reach trivial chain
(defrule backtrace
    (bt ?x ?y ?d)
    (chain ?x ?y ?d ?v)   
    (test (>= ?d 1))
    =>
    (printout t ?x " to " ?y " via " ?v ", distance " ?d crlf)
    (assert(bt ?v ?y (- ?d 1)))
;;; 
;;; add bt fact for v-y chain
;;;
)

(assert
    (path "a" "b")
    (path "b" "c")
    (path "c" "d")
    (path "d" "e")
    (path "e" "f")
    (path "f" "g")
    (path "d" "h")
    (path "h" "i")
)

(assert 
    (query "i" "g")
)

(run)
(facts)
