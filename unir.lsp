;;; Cread=o por Freddy Molina
;;; unir puntos con poliLineas
;;; selecciona los puntos del grafico y los une
;;; con una poliLinea...

(defun une (p / dp dl)
  (setq dp p)(setq dl (length p)) (command "PLINE")
  (repeat dl (command (car dp)) (setq dp (cdr dp)) )
  (command "c")(princ)
)
(defun c:unir (/ block sel index n ent p1 pl)
(setq sel (ssget "x" (list (cons 0 "POINT"))))
(setq n (sslength sel) index 0)(repeat n
(setq ent (cdr (car (entget (ssname sel index)))))
(setq index (1+ index))(prompt ">")
(setq p1 (cdr (assoc 10 (entget ent))))
(setq pl (cons p1 pl))
)
(une pl)
(princ)
)