(ns example
  (:require [clojure.string :as str]))

(def data
  (str/split-lines (slurp "data.csv")))

(def headers
  (str/split (first data) #","))

(defn list-data []
  (mapv #(zipmap headers
                 (str/split % #","))
       (rest data)))



