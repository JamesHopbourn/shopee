#!/usr/bin/env python3


woman = ["BR34=EU36=22.5CM=US5.5",
"BR34.5=EU36.5=23CM=US6",
"BR35.5=EU37=23.5CM=US6.5",
"BR36=EU38=24CM=US7",
"BR36.5=EU38.5=24.5CM=US7.5",
"BR37=EU39=25CM=US8"
]

man = [
	"BR38=EU40=25CM=US7",
	"BR38.5=EU40.5=25.5cm=US7.5",
	"BR39=EU41=26CM=US8",
	"BR40=EU42=26.5CM=US8.5",
	"BR40.5=EU42.5=27CM=US9",
	"BR41=EU43=27.5CM=US9.5",
	"BR42=EU44=28CM=US10",
	"BR42.5=EU44.5=28.5CM=US10.5",
	"BR43=EU45=29CM=US11",
	"BR44=EUR46=29.5CM=US11.5"
]

universal = woman + man

gender_mapper = {
	"女": woman,
	"男": man,
	"皆宜": universal
}
print(gender_mapper['男'])
