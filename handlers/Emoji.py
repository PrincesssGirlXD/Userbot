#~ Ported from Cat

from pyrogram import *
from pyrogram.types import *
from handlers.help import *

from helpers.basic import edit_or_reply, get_text


kakashitext = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]


kakashiemoji = [
    "ā­\n                    š\n                  šš\n               ššš\n            šš šš\n          šš    šš\n        šš       šš\n      šššššš\n     ššššššš\n   šš                 šš\n  šš                    šš\nšš                       šš\n",
    "ā­\nššššššš\nšššššššš\nšš                     šš\nšš                     šš\nšššššššš\nšššššššš\nšš                     šš\nšš                     šš\nšššššššš\nššššššš\n",
    "ā­\n          šššššš\n     šššššššš\n   šš                      šš\n šš\nšš\nšš\n šš\n   šš                      šš\n     šššššššš\n         šššššš\n",
    "ā­\nššššššš\nšššššššš\nšš                      šš\nšš                         šš\nšš                         šš\nšš                         šš\nšš                         šš\nšš                      šš\nšššššššš\nššššššš\n",
    "ā­\nšššššššš\nšššššššš\nšš\nšš\nšššššš\nšššššš\nšš\nšš\nšššššššš\nšššššššš\n",
    "ā­\nšššššššš\nšššššššš\nšš\nšš\nšššššš\nšššššš\nšš\nšš\nšš\nšš\n",
    "ā­\n          šššššš\n     šššššššš\n   šš                     šš\n šš\nšš                šššš\nšš                šššš\n šš                        šš\n   šš                      šš\n     šššššššš\n          šššššš\n",
    "ā­\nšš                        šš\nšš                        šš\nšš                        šš\nšš                        šš\nššššššššš\nššššššššš\nšš                        šš\nšš                        šš\nšš                        šš\nšš                        šš\n",
    "ā­\nšššššš\nšššššš\n          šš\n          šš\n          šš\n          šš\n          šš\n          šš\nšššššš\nšššššš\n",
    "ā­\n         šššššš\n         šššššš\n                  šš\n                  šš\n                  šš\n                  šš\nšš          šš\n  šš       šš\n   ššššš\n      šššš\n",
    "ā­\nšš                  šš\nšš             šš\nšš        šš\nšš   šš\nšššš\nšš šš\nšš     šš\nšš         šš\nšš              šš\nšš                   šš\n",
    "ā­\nšš\nšš\nšš\nšš\nšš\nšš\nšš\nšš\nšššššššš\nšššššššš\n",
    "ā­\nšš                              šš\nššš                      ššš\nšššš            šššš\nšš    šš    šš    šš\nšš        ššš        šš\nšš             š             šš\nšš                              šš\nšš                              šš\nšš                              šš\nšš                              šš\n",
    "ā­\nšš                           šš\nššš                       šš\nšššš                 šš\nšš  šš               šš\nšš     šš            šš\nšš         šš        šš\nšš             šš    šš\nšš                 šššš\nšš                     ššš\nšš                          šš\n",
    "ā­\n           ššššš\n     ššššššš\n   šš                   šš\n šš                       šš\nšš                         šš\nšš                         šš\n šš                       šš\n   šš                   šš\n      ššššššš\n            ššššš\n",
    "ā­\nššššššš\nšššššššš\nšš                     šš\nšš                     šš\nšššššššš\nššššššš\nšš\nšš\nšš\nšš\n",
    "ā­\n           ššššš\n      ššššššš\n   šš                    šš\n šš                        šš\nšš                           šš\nšš              šš     šš\n šš               šš šš\n   šš                   šš\n      šššššššš\n           ššššš   šš\n",
    "ā­\nššššššš\nšššššššš\nšš                     šš\nšš                     šš\nšššššššš\nššššššš\nšš    šš\nšš         šš\nšš              šš\nšš                  šš\n",
    "ā­\n       ššššš\n  ššššššš\n  šš                 šš\nšš\n  šššššš\n      šššššš\n                            šš\nšš                 šš\n  ššššššš\n       ššššš\n",
    "ā­\nšššššššš\nšššššššš\n               šš\n               šš\n               šš\n               šš\n               šš\n               šš\n               šš\n",
    "ā­\nšš                      šš\nšš                      šš\nšš                      šš\nšš                      šš\nšš                      šš\nšš                      šš\nšš                      šš\n  šš                  šš\n      šššššš\n            šššš\n",
    "ā­\nšš                              šš\n  šš                          šš\n    šš                      šš\n      šš                  šš\n         šš              šš\n           šš         šš\n             šš     šš\n               šš šš\n                  ššš\n                       š\n",
    "ā­\nšš                               šš\nšš                               šš\nšš                               šš\nšš                               šš\nšš              š            šš\n šš           šš          šš\n šš        ššš       šš\n  šš   šš  šš   šš\n   šššš      šššš\n    ššš             ššš\n",
    "ā­\nšš                    šš\n   šš              šš\n      šš        šš\n         šš  šš\n            ššš\n            ššš\n         šš šš\n      šš       šš\n   šš             šš\nšš                   šš\n",
    "ā­\nšš                    šš\n   šš              šš\n      šš        šš\n         šš  šš\n            ššš\n              šš\n              šš\n              šš\n              šš\n              šš\n",
    "ā­\n ššššššš\n ššššššš\n                       šš\n                   šš\n               šš\n           šš\n       šš\n   šš\nššššššš\nššššššš\n",
    "ā­\n       šššš\n   šššššš\nšš               šš\nšš               šš\nšš               šš\nšš               šš\nšš               šš\nšš               šš\n   šššššš\n        šššš\n",
    "ā­\n          šš\n     ššš\nšš šš\n          šš\n          šš\n          šš\n          šš\n          šš\n     šššš\n     šššš\n",
    "ā­\n    ššššš\n  šššššš\nšš          šš\n                šš\n             šš\n          šš\n       šš\n    šš\n  šššššš\n  šššššš\n",
    "ā­\n     šššš\n  ššššš\nšš         šš\n                   šš\n            ššš\n            ššš\n                   šš\nšš         šš\n  ššššš\n     šššš\n",
    "ā­\n                         šš\n                    ššš\n              šš šš\n          šš     šš\n     šš          šš\nšš               šš\nššššššššš\nššššššššš\n                         šš\n                         šš\n",
    "ā­\nšššššš\nšššššš\nšš\n ššššš\n   ššššš\n                    šš\n                    šš\nšš          šš\n  ššššš\n     šššš\n",
    "ā­\n        šššš\n    ššššš\nšš\n\nšš\nšššššš\nššššššš\nšš               šš\nšš               šš\n    šššššš\n        šššš\n",
    "ā­\nššššššš\nššššššš\n                      šš\n                     šš\n                   šš\n                 šš\n               šš\n             šš\n           šš\n         šš\n",
    "ā­\n        šššš\n   šššššš\nšš               šš\nšš               šš\n   šššššš\n   šššššš\nšš               šš\nšš               šš\n   šššššš\n        šššš\n",
    "ā­\n        šššš\n   šššššš\nšš               šš\nšš               šš\n ššššššš\n      šššššš\n                         šš\n                        šš\n  šššššš\n       šššš\n",
]


itachiemoji = [
    "ā­\n                    {cj}\n                  {cj}{cj}\n               {cj}{cj}{cj}\n            {cj}{cj} {cj}{cj}\n          {cj}{cj}    {cj}{cj}\n        {cj}{cj}       {cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}                 {cj}{cj}\n  {cj}{cj}                    {cj}{cj}\n{cj}{cj}                       {cj}{cj}\n",
    "ā­\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "ā­\n          {cj}{cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}                      {cj}{cj}\n {cj}{cj}\n{cj}{cj}\n{cj}{cj}\n {cj}{cj}\n   {cj}{cj}                      {cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n         {cj}{cj}{cj}{cj}{cj}{cj}\n",
    "ā­\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "ā­\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "ā­\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n",
    "ā­\n          {cj}{cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}                     {cj}{cj}\n {cj}{cj}\n{cj}{cj}                {cj}{cj}{cj}{cj}\n{cj}{cj}                {cj}{cj}{cj}{cj}\n {cj}{cj}                        {cj}{cj}\n   {cj}{cj}                      {cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n          {cj}{cj}{cj}{cj}{cj}{cj}\n",
    "ā­\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n{cj}{cj}                        {cj}{cj}\n",
    "ā­\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "ā­\n         {cj}{cj}{cj}{cj}{cj}{cj}\n         {cj}{cj}{cj}{cj}{cj}{cj}\n                  {cj}{cj}\n                  {cj}{cj}\n                  {cj}{cj}\n                  {cj}{cj}\n{cj}{cj}          {cj}{cj}\n  {cj}{cj}       {cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}\n      {cj}{cj}{cj}{cj}\n",
    "ā­\n{cj}{cj}                  {cj}{cj}\n{cj}{cj}             {cj}{cj}\n{cj}{cj}        {cj}{cj}\n{cj}{cj}   {cj}{cj}\n{cj}{cj}{cj}{cj}\n{cj}{cj} {cj}{cj}\n{cj}{cj}     {cj}{cj}\n{cj}{cj}         {cj}{cj}\n{cj}{cj}              {cj}{cj}\n{cj}{cj}                   {cj}{cj}\n",
    "ā­\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "ā­\n{cj}{cj}                              {cj}{cj}\n{cj}{cj}{cj}                      {cj}{cj}{cj}\n{cj}{cj}{cj}{cj}            {cj}{cj}{cj}{cj}\n{cj}{cj}    {cj}{cj}    {cj}{cj}    {cj}{cj}\n{cj}{cj}        {cj}{cj}{cj}        {cj}{cj}\n{cj}{cj}             {cj}             {cj}{cj}\n{cj}{cj}                              {cj}{cj}\n{cj}{cj}                              {cj}{cj}\n{cj}{cj}                              {cj}{cj}\n{cj}{cj}                              {cj}{cj}\n",
    "ā­\n{cj}{cj}                           {cj}{cj}\n{cj}{cj}{cj}                       {cj}{cj}\n{cj}{cj}{cj}{cj}                 {cj}{cj}\n{cj}{cj}  {cj}{cj}               {cj}{cj}\n{cj}{cj}     {cj}{cj}            {cj}{cj}\n{cj}{cj}         {cj}{cj}        {cj}{cj}\n{cj}{cj}             {cj}{cj}    {cj}{cj}\n{cj}{cj}                 {cj}{cj}{cj}{cj}\n{cj}{cj}                     {cj}{cj}{cj}\n{cj}{cj}                          {cj}{cj}\n",
    "ā­\n           {cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}                   {cj}{cj}\n {cj}{cj}                       {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n{cj}{cj}                         {cj}{cj}\n {cj}{cj}                       {cj}{cj}\n   {cj}{cj}                   {cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n            {cj}{cj}{cj}{cj}{cj}\n",
    "ā­\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n{cj}{cj}\n",
    "ā­\n           {cj}{cj}{cj}{cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}                    {cj}{cj}\n {cj}{cj}                        {cj}{cj}\n{cj}{cj}                           {cj}{cj}\n{cj}{cj}              {cj}{cj}     {cj}{cj}\n {cj}{cj}               {cj}{cj} {cj}{cj}\n   {cj}{cj}                   {cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n           {cj}{cj}{cj}{cj}{cj}   {cj}{cj}\n",
    "ā­\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}                     {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}    {cj}{cj}\n{cj}{cj}         {cj}{cj}\n{cj}{cj}              {cj}{cj}\n{cj}{cj}                  {cj}{cj}\n",
    "ā­\n       {cj}{cj}{cj}{cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n  {cj}{cj}                 {cj}{cj}\n{cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}\n                            {cj}{cj}\n{cj}{cj}                 {cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n       {cj}{cj}{cj}{cj}{cj}\n",
    "ā­\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n               {cj}{cj}\n",
    "ā­\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n{cj}{cj}                      {cj}{cj}\n  {cj}{cj}                  {cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}\n            {cj}{cj}{cj}{cj}\n",
    "ā­\n{cj}{cj}                              {cj}{cj}\n  {cj}{cj}                          {cj}{cj}\n    {cj}{cj}                      {cj}{cj}\n      {cj}{cj}                  {cj}{cj}\n         {cj}{cj}              {cj}{cj}\n           {cj}{cj}         {cj}{cj}\n             {cj}{cj}     {cj}{cj}\n               {cj}{cj} {cj}{cj}\n                  {cj}{cj}{cj}\n                       {cj}\n",
    "ā­\n{cj}{cj}                               {cj}{cj}\n{cj}{cj}                               {cj}{cj}\n{cj}{cj}                               {cj}{cj}\n{cj}{cj}                               {cj}{cj}\n{cj}{cj}              {cj}            {cj}{cj}\n {cj}{cj}           {cj}{cj}          {cj}{cj}\n {cj}{cj}        {cj}{cj}{cj}       {cj}{cj}\n  {cj}{cj}   {cj}{cj}  {cj}{cj}   {cj}{cj}\n   {cj}{cj}{cj}{cj}      {cj}{cj}{cj}{cj}\n    {cj}{cj}{cj}             {cj}{cj}{cj}\n",
    "ā­\n{cj}{cj}                    {cj}{cj}\n   {cj}{cj}              {cj}{cj}\n      {cj}{cj}        {cj}{cj}\n         {cj}{cj}  {cj}{cj}\n            {cj}{cj}{cj}\n            {cj}{cj}{cj}\n         {cj}{cj} {cj}{cj}\n      {cj}{cj}       {cj}{cj}\n   {cj}{cj}             {cj}{cj}\n{cj}{cj}                   {cj}{cj}\n",
    "ā­\n{cj}{cj}                    {cj}{cj}\n   {cj}{cj}              {cj}{cj}\n      {cj}{cj}        {cj}{cj}\n         {cj}{cj}  {cj}{cj}\n            {cj}{cj}{cj}\n              {cj}{cj}\n              {cj}{cj}\n              {cj}{cj}\n              {cj}{cj}\n              {cj}{cj}\n",
    "ā­\n {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n                       {cj}{cj}\n                   {cj}{cj}\n               {cj}{cj}\n           {cj}{cj}\n       {cj}{cj}\n   {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n",
    "ā­\n       {cj}{cj}{cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n        {cj}{cj}{cj}{cj}\n",
    "ā­\n          {cj}{cj}\n     {cj}{cj}{cj}\n{cj}{cj} {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n          {cj}{cj}\n     {cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}\n",
    "ā­\n    {cj}{cj}{cj}{cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}          {cj}{cj}\n                {cj}{cj}\n             {cj}{cj}\n          {cj}{cj}\n       {cj}{cj}\n    {cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}\n",
    "ā­\n     {cj}{cj}{cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}\n{cj}{cj}         {cj}{cj}\n                   {cj}{cj}\n            {cj}{cj}{cj}\n            {cj}{cj}{cj}\n                   {cj}{cj}\n{cj}{cj}         {cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}\n",
    "ā­\n                         {cj}{cj}\n                    {cj}{cj}{cj}\n              {cj}{cj} {cj}{cj}\n          {cj}{cj}     {cj}{cj}\n     {cj}{cj}          {cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n                         {cj}{cj}\n                         {cj}{cj}\n",
    "ā­\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n {cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}\n                    {cj}{cj}\n                    {cj}{cj}\n{cj}{cj}          {cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}\n     {cj}{cj}{cj}{cj}\n",
    "ā­\n        {cj}{cj}{cj}{cj}\n    {cj}{cj}{cj}{cj}{cj}\n{cj}{cj}\n\n{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n    {cj}{cj}{cj}{cj}{cj}{cj}\n        {cj}{cj}{cj}{cj}\n",
    "ā­\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}{cj}{cj}{cj}{cj}{cj}\n                      {cj}{cj}\n                     {cj}{cj}\n                   {cj}{cj}\n                 {cj}{cj}\n               {cj}{cj}\n             {cj}{cj}\n           {cj}{cj}\n         {cj}{cj}\n",
    "ā­\n        {cj}{cj}{cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n        {cj}{cj}{cj}{cj}\n",
    "ā­\n        {cj}{cj}{cj}{cj}\n   {cj}{cj}{cj}{cj}{cj}{cj}\n{cj}{cj}               {cj}{cj}\n{cj}{cj}               {cj}{cj}\n {cj}{cj}{cj}{cj}{cj}{cj}{cj}\n      {cj}{cj}{cj}{cj}{cj}{cj}\n                         {cj}{cj}\n                        {cj}{cj}\n  {cj}{cj}{cj}{cj}{cj}{cj}\n       {cj}{cj}{cj}{cj}\n",
]


@Client.on_message(filters.command('emoji', ["-"]) & filters.me)
async def emoji(client: Client, message: Message):
    op = await edit_or_reply(message, "`Emojifying the text..`")
    args = get_text(message)
    if not args:
        if not message.reply_to_message:
           return await ok.edit("__What am I Supposed to do with this idiot, Give me a text.__")
        if not message.reply_to_message.text:
           return await ok.edit("__What am I Supposed to do with this idiot, Give me a text.__")
    args = args or message.reply_to_message.text
    
    result = ""
    for a in args:
        a = a.lower()
        if a in kakashitext:
            char = kakashiemoji[kakashitext.index(a)]
            result += char
        else:
            result += a
    await op.edit(result)
    
    


@Client.on_message(filters.command('cmoji', ["-"]) & filters.me)
async def cmoji(client: Client, message: Message):
    op = await edit_or_reply(message, "`Emojifying the text..`")
    args = get_text(message)
    if not args:
        if not message.reply_to_message:
           return await ok.edit("__What am I Supposed to do with this idiot, Give me a text.__")
        if not message.reply_to_message.text:
           return await ok.edit("__What am I Supposed to do with this idiot, Give me a text.__")
    args = args or message.reply_to_message.text
    try:
        emoji, arg = args.split(" ", 1)
    except Exception:
        arg = args
        emoji = "š"
    result = ""
    for a in arg:
        a = a.lower()
        if a in kakashitext:
            char = itachiemoji[kakashitext.index(a)].format(cj=emoji)
            result += char
        else:
            result += a
    await op.edit(result)


add_command_help(
    "emoji",
    [
        [".emoji", "To Make Your Custom Emoji With Reply."],
        [".cmoji", "make A Message with Emoji."],
    ],
)
