(ns clj-example.clj
  (:require [clojure.string :as str])
  (:gen-class))


(def data
  (str/split-lines (slurp "resources/data.csv")))

(def headers
  (str/split (first data) #","))

(defn list-data []
  (mapv #(zipmap headers
                 (str/split % #","))
        (rest data)))

(defn -main
  "List humanitarian data from 2014."
  []
  (list-data))
